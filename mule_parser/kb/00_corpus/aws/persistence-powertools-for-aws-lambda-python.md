# Persistence - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/persistence](https://docs.aws.amazon.com/powertools/python/latest/api_doc/circuit_breaker_alpha/persistence)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Store circuit state in an Amazon DynamoDB table, one item per circuit.

The class name is prefixed with CircuitBreaker so a function using both the
Idempotency and Circuit Breaker utilities can import both persistence layers
without an alias.

PARAMETER

DESCRIPTION

table_name

Name of the DynamoDB table that stores circuit state.

Sort key attribute holding the circuit name. When set, the table is treated as
composite: static_pk_value is written to the partition key and the circuit
name to the sort key. Omit it for the default partition-key-only behavior.

def__init__(self,table_name:str,key_attr:str="id",static_pk_value:str|None=None,sort_key_attr:str|None=None,state_attr:str="state",failure_count_attr:str="failure_count",opened_at_attr:str="opened_at",half_open_owner_attr:str="half_open_owner",probe_lease_expiry_attr:str="probe_lease_expiry",expiry_attr:str="expiration",boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:DynamoDBClient|None=None,):ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("dynamodb",config=boto_config)self.client=boto3_clientuser_agent.register_feature_to_client(client=self.client,feature="circuit_breaker")ifsort_key_attr==key_attr:raiseCircuitBreakerConfigError(f"key_attr [{key_attr}] and sort_key_attr [{sort_key_attr}] cannot be the same!",)ifstatic_pk_valueisnotNoneandsort_key_attrisNone:warnings.warn("static_pk_value is ignored unless sort_key_attr is also set.",category=PowertoolsUserWarning,stacklevel=2,)ifstatic_pk_valueisNone:static_pk_value=f"circuit_breaker#{os.getenv(constants.LAMBDA_FUNCTION_NAME_ENV,'')}"self.table_name=table_nameself.key_attr=key_attrself.static_pk_value=static_pk_valueself.sort_key_attr=sort_key_attrself.state_attr=state_attrself.failure_count_attr=failure_count_attrself.opened_at_attr=opened_at_attrself.half_open_owner_attr=half_open_owner_attrself.probe_lease_expiry_attr=probe_lease_expiry_attrself.expiry_attr=expiry_attrself._deserializer=TypeDeserializer()super().__init__()

Abstract base class for circuit breaker persistence layers.

Owns the per-environment read cache and the fail-open behavior. Subclasses
implement :meth:_get_record, :meth:_put_record, and :meth:_update_record
for a specific store.

A persistence layer is keyed by circuit name, not by a payload hash, which is
the main reason it does not reuse the Idempotency persistence layer.

Atomically elect a single worker to run the half-open probe.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

63646566676869707172737475767778

def__init__(self)->None:"""Initialize defaults; real configuration happens in :meth:`configure`."""# Per-circuit tunables, keyed by circuit name. One persistence instance is shared# by every circuit (and thread) using the same store, so these must never live in# plain instance attributes: circuits with different configs would stamp each# other's TTL and probe lease. A plain dict, not an LRUDict: evicting a live# circuit's settings would silently swap in the defaults (wrong lease and TTL),# whereas evicting a cache entry below only costs a store re-read.self._settings:dict[str,_CircuitSettings]={}# Maps circuit name -> the unix timestamp the locally cached record goes stale.# Kept separate from the record's durable ``expiry_timestamp`` (the store TTL) so# the short in-memory freshness window is never mistaken for the long store TTL.self._cache:LRUDict=LRUDict(max_items=LOCAL_CACHE_MAX_ITEMS)# One lock for both maps: LRUDict reorders entries even on reads, so unguarded# concurrent access can corrupt it or raise.self._lock=threading.Lock()

Called once per invocation by the handler; the assignment is cheap and the
same persistence instance is reused across invocations within an environment.

PARAMETER

DESCRIPTION

config

Configuration providing the local cache TTL and recovery timeout.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

80818283848586878889909192939495969798

defconfigure(self,config:CircuitBreakerConfig,circuit_name:str)->None:""" Bind a circuit's configuration to the layer. Called once per invocation by the handler; the assignment is cheap and the same persistence instance is reused across invocations within an environment. Parameters ---------- config : CircuitBreakerConfig Configuration providing the local cache TTL and recovery timeout. circuit_name : str The circuit these settings apply to. """withself._lock:self._settings[circuit_name]=_CircuitSettings(local_cache_max_age=config.local_cache_max_age,recovery_timeout=config.recovery_timeout,)

Return the current circuit state, reading the store only on a cache miss.

A cache miss (cold start or expired local entry) forces a read-through before
the caller routes the request, so a freshly started environment never assumes a
circuit is closed without checking.

Fail-open: if the store read itself raises, the circuit is treated as
CLOSED. A circuit breaker must never become the outage it is meant to
prevent.

defget_state(self,name:str)->CircuitStateRecord:""" Return the current circuit state, reading the store only on a cache miss. A cache miss (cold start or expired local entry) forces a read-through before the caller routes the request, so a freshly started environment never assumes a circuit is closed without checking. Fail-open: if the store read itself raises, the circuit is treated as ``CLOSED``. A circuit breaker must never become the outage it is meant to prevent. Parameters ---------- name : str Circuit name. Returns ------- CircuitStateRecord The current record, a synthesized closed record if none exists yet, or a synthesized closed record if the store could not be reached. """cached=self._retrieve_from_cache(name)ifcachedisnotNone:returncachedtry:record=self._get_record(name)exceptException:# Fail open without caching, so the next invocation retries the store rather# than serving a synthesized CLOSED for the whole local cache window.logger.warning("Failed to read circuit state for '%s'; failing open (treating as CLOSED).",name,exc_info=True,)returnCircuitStateRecord(name=name,state=CircuitState.CLOSED)# A missing record is the expected cold-start case, not a failure: treat it as a# closed circuit and cache it like any other read.ifrecordisNone:record=CircuitStateRecord(name=name,state=CircuitState.CLOSED)self._save_to_cache(record)returnrecord

Persist a transition back to CLOSED and reset counters.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

261262263264265266267268269270

defsave_closed(self,name:str)->None:"""Persist a transition back to CLOSED and reset counters."""record=CircuitStateRecord(name=name,state=CircuitState.CLOSED,failure_count=0,expiry_timestamp=self._durable_ttl(name),)self._update_record(record)self._save_to_cache(record)

defsave_open(self,name:str,failure_count:int,opened_at:int)->None:""" Persist a CLOSED to OPEN transition. Parameters ---------- name : str Circuit name. failure_count : int Consecutive failures that tripped the circuit. opened_at : int Unix timestamp the circuit opened; anchors the recovery timeout. """record=CircuitStateRecord(name=name,state=CircuitState.OPEN,failure_count=failure_count,opened_at=opened_at,expiry_timestamp=self._durable_ttl(name),)self._put_record(record)self._save_to_cache(record)

Persist a HALF_OPEN to OPEN transition after a failed probe.

If this write fails the stored row stays in HALF_OPEN, but it does not strand the
circuit: the probe lease expiry still applies, so once it lapses another
environment wins the next election and drives the transition.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

272273274275276277278279280281282283284285286287

defsave_reopen(self,name:str,opened_at:int)->None:""" Persist a HALF_OPEN to OPEN transition after a failed probe. If this write fails the stored row stays in HALF_OPEN, but it does not strand the circuit: the probe lease expiry still applies, so once it lapses another environment wins the next election and drives the transition. """record=CircuitStateRecord(name=name,state=CircuitState.OPEN,opened_at=opened_at,expiry_timestamp=self._durable_ttl(name),)self._update_record(record)self._save_to_cache(record)

Atomically elect a single worker to run the half-open probe.

The conditional write succeeds only when the circuit is OPEN with no existing
lock owner AND the opened_at matches what the caller observed (guards against
stale eventually-consistent reads). A lease expiry is stamped so that if the
winning worker is recycled before completing the probe, others can take over
once the lease lapses.

deftry_acquire_half_open(self,name:str,owner:str,opened_at:int)->bool:""" Atomically elect a single worker to run the half-open probe. The conditional write succeeds only when the circuit is OPEN with no existing lock owner AND the ``opened_at`` matches what the caller observed (guards against stale eventually-consistent reads). A lease expiry is stamped so that if the winning worker is recycled before completing the probe, others can take over once the lease lapses. Parameters ---------- name : str Circuit name. owner : str Identifier of the worker (one thread in one execution environment) attempting the probe. opened_at : int The ``opened_at`` the caller observed, kept stable across the transition. Returns ------- bool ``True`` if this worker won the probe lock, ``False`` if another worker already holds it. """# Lease = recovery_timeout gives the probe a full cycle to complete.probe_lease_expiry=int(datetime.datetime.now().timestamp())+self._settings_for(name).recovery_timeoutrecord=CircuitStateRecord(name=name,state=CircuitState.HALF_OPEN,opened_at=opened_at,half_open_owner=owner,probe_lease_expiry=probe_lease_expiry,expiry_timestamp=self._durable_ttl(name),)try:self._put_record(record,condition="half_open",expected_opened_at=opened_at)exceptCircuitBreakerExistingLockError:returnFalseself._save_to_cache(record)returnTrue

One record exists per circuit name. This is the utility's internal representation;
user code never sees it directly, only the CircuitInfo produced by
:meth:to_circuit_info.

PARAMETER

DESCRIPTION

name

Circuit name, used as the partition key in the store.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/record.py

474849505152535455565758596061626364

defto_circuit_info(self)->CircuitInfo:""" Project this record to the public ``CircuitInfo`` handed to user code. Strips internal fields (``half_open_owner``, ``expiry_timestamp``) so no persistence detail leaks across the public boundary. Returns ------- CircuitInfo Public snapshot of the circuit. """returnCircuitInfo(name=self.name,state=self.state,failure_count=self.failure_count,opened_at=self.opened_at,)

Abstract persistence layer for the Circuit Breaker utility.

Concrete backends (DynamoDB, cache) subclass :class:CircuitBreakerPersistenceLayer
and implement the small set of store primitives. The base class owns the local
read-through cache and the fail-open policy so every backend behaves identically.

Abstract base class for circuit breaker persistence layers.

Owns the per-environment read cache and the fail-open behavior. Subclasses
implement :meth:_get_record, :meth:_put_record, and :meth:_update_record
for a specific store.

A persistence layer is keyed by circuit name, not by a payload hash, which is
the main reason it does not reuse the Idempotency persistence layer.

Atomically elect a single worker to run the half-open probe.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

63646566676869707172737475767778

def__init__(self)->None:"""Initialize defaults; real configuration happens in :meth:`configure`."""# Per-circuit tunables, keyed by circuit name. One persistence instance is shared# by every circuit (and thread) using the same store, so these must never live in# plain instance attributes: circuits with different configs would stamp each# other's TTL and probe lease. A plain dict, not an LRUDict: evicting a live# circuit's settings would silently swap in the defaults (wrong lease and TTL),# whereas evicting a cache entry below only costs a store re-read.self._settings:dict[str,_CircuitSettings]={}# Maps circuit name -> the unix timestamp the locally cached record goes stale.# Kept separate from the record's durable ``expiry_timestamp`` (the store TTL) so# the short in-memory freshness window is never mistaken for the long store TTL.self._cache:LRUDict=LRUDict(max_items=LOCAL_CACHE_MAX_ITEMS)# One lock for both maps: LRUDict reorders entries even on reads, so unguarded# concurrent access can corrupt it or raise.self._lock=threading.Lock()

Called once per invocation by the handler; the assignment is cheap and the
same persistence instance is reused across invocations within an environment.

PARAMETER

DESCRIPTION

config

Configuration providing the local cache TTL and recovery timeout.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

80818283848586878889909192939495969798

defconfigure(self,config:CircuitBreakerConfig,circuit_name:str)->None:""" Bind a circuit's configuration to the layer. Called once per invocation by the handler; the assignment is cheap and the same persistence instance is reused across invocations within an environment. Parameters ---------- config : CircuitBreakerConfig Configuration providing the local cache TTL and recovery timeout. circuit_name : str The circuit these settings apply to. """withself._lock:self._settings[circuit_name]=_CircuitSettings(local_cache_max_age=config.local_cache_max_age,recovery_timeout=config.recovery_timeout,)

Return the current circuit state, reading the store only on a cache miss.

A cache miss (cold start or expired local entry) forces a read-through before
the caller routes the request, so a freshly started environment never assumes a
circuit is closed without checking.

Fail-open: if the store read itself raises, the circuit is treated as
CLOSED. A circuit breaker must never become the outage it is meant to
prevent.

defget_state(self,name:str)->CircuitStateRecord:""" Return the current circuit state, reading the store only on a cache miss. A cache miss (cold start or expired local entry) forces a read-through before the caller routes the request, so a freshly started environment never assumes a circuit is closed without checking. Fail-open: if the store read itself raises, the circuit is treated as ``CLOSED``. A circuit breaker must never become the outage it is meant to prevent. Parameters ---------- name : str Circuit name. Returns ------- CircuitStateRecord The current record, a synthesized closed record if none exists yet, or a synthesized closed record if the store could not be reached. """cached=self._retrieve_from_cache(name)ifcachedisnotNone:returncachedtry:record=self._get_record(name)exceptException:# Fail open without caching, so the next invocation retries the store rather# than serving a synthesized CLOSED for the whole local cache window.logger.warning("Failed to read circuit state for '%s'; failing open (treating as CLOSED).",name,exc_info=True,)returnCircuitStateRecord(name=name,state=CircuitState.CLOSED)# A missing record is the expected cold-start case, not a failure: treat it as a# closed circuit and cache it like any other read.ifrecordisNone:record=CircuitStateRecord(name=name,state=CircuitState.CLOSED)self._save_to_cache(record)returnrecord

Persist a transition back to CLOSED and reset counters.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

261262263264265266267268269270

defsave_closed(self,name:str)->None:"""Persist a transition back to CLOSED and reset counters."""record=CircuitStateRecord(name=name,state=CircuitState.CLOSED,failure_count=0,expiry_timestamp=self._durable_ttl(name),)self._update_record(record)self._save_to_cache(record)

defsave_open(self,name:str,failure_count:int,opened_at:int)->None:""" Persist a CLOSED to OPEN transition. Parameters ---------- name : str Circuit name. failure_count : int Consecutive failures that tripped the circuit. opened_at : int Unix timestamp the circuit opened; anchors the recovery timeout. """record=CircuitStateRecord(name=name,state=CircuitState.OPEN,failure_count=failure_count,opened_at=opened_at,expiry_timestamp=self._durable_ttl(name),)self._put_record(record)self._save_to_cache(record)

Persist a HALF_OPEN to OPEN transition after a failed probe.

If this write fails the stored row stays in HALF_OPEN, but it does not strand the
circuit: the probe lease expiry still applies, so once it lapses another
environment wins the next election and drives the transition.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/base.py

272273274275276277278279280281282283284285286287

defsave_reopen(self,name:str,opened_at:int)->None:""" Persist a HALF_OPEN to OPEN transition after a failed probe. If this write fails the stored row stays in HALF_OPEN, but it does not strand the circuit: the probe lease expiry still applies, so once it lapses another environment wins the next election and drives the transition. """record=CircuitStateRecord(name=name,state=CircuitState.OPEN,opened_at=opened_at,expiry_timestamp=self._durable_ttl(name),)self._update_record(record)self._save_to_cache(record)

Atomically elect a single worker to run the half-open probe.

The conditional write succeeds only when the circuit is OPEN with no existing
lock owner AND the opened_at matches what the caller observed (guards against
stale eventually-consistent reads). A lease expiry is stamped so that if the
winning worker is recycled before completing the probe, others can take over
once the lease lapses.

deftry_acquire_half_open(self,name:str,owner:str,opened_at:int)->bool:""" Atomically elect a single worker to run the half-open probe. The conditional write succeeds only when the circuit is OPEN with no existing lock owner AND the ``opened_at`` matches what the caller observed (guards against stale eventually-consistent reads). A lease expiry is stamped so that if the winning worker is recycled before completing the probe, others can take over once the lease lapses. Parameters ---------- name : str Circuit name. owner : str Identifier of the worker (one thread in one execution environment) attempting the probe. opened_at : int The ``opened_at`` the caller observed, kept stable across the transition. Returns ------- bool ``True`` if this worker won the probe lock, ``False`` if another worker already holds it. """# Lease = recovery_timeout gives the probe a full cycle to complete.probe_lease_expiry=int(datetime.datetime.now().timestamp())+self._settings_for(name).recovery_timeoutrecord=CircuitStateRecord(name=name,state=CircuitState.HALF_OPEN,opened_at=opened_at,half_open_owner=owner,probe_lease_expiry=probe_lease_expiry,expiry_timestamp=self._durable_ttl(name),)try:self._put_record(record,condition="half_open",expected_opened_at=opened_at)exceptCircuitBreakerExistingLockError:returnFalseself._save_to_cache(record)returnTrue

Store circuit state in an Amazon DynamoDB table, one item per circuit.

The class name is prefixed with CircuitBreaker so a function using both the
Idempotency and Circuit Breaker utilities can import both persistence layers
without an alias.

PARAMETER

DESCRIPTION

table_name

Name of the DynamoDB table that stores circuit state.

Sort key attribute holding the circuit name. When set, the table is treated as
composite: static_pk_value is written to the partition key and the circuit
name to the sort key. Omit it for the default partition-key-only behavior.

def__init__(self,table_name:str,key_attr:str="id",static_pk_value:str|None=None,sort_key_attr:str|None=None,state_attr:str="state",failure_count_attr:str="failure_count",opened_at_attr:str="opened_at",half_open_owner_attr:str="half_open_owner",probe_lease_expiry_attr:str="probe_lease_expiry",expiry_attr:str="expiration",boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:DynamoDBClient|None=None,):ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("dynamodb",config=boto_config)self.client=boto3_clientuser_agent.register_feature_to_client(client=self.client,feature="circuit_breaker")ifsort_key_attr==key_attr:raiseCircuitBreakerConfigError(f"key_attr [{key_attr}] and sort_key_attr [{sort_key_attr}] cannot be the same!",)ifstatic_pk_valueisnotNoneandsort_key_attrisNone:warnings.warn("static_pk_value is ignored unless sort_key_attr is also set.",category=PowertoolsUserWarning,stacklevel=2,)ifstatic_pk_valueisNone:static_pk_value=f"circuit_breaker#{os.getenv(constants.LAMBDA_FUNCTION_NAME_ENV,'')}"self.table_name=table_nameself.key_attr=key_attrself.static_pk_value=static_pk_valueself.sort_key_attr=sort_key_attrself.state_attr=state_attrself.failure_count_attr=failure_count_attrself.opened_at_attr=opened_at_attrself.half_open_owner_attr=half_open_owner_attrself.probe_lease_expiry_attr=probe_lease_expiry_attrself.expiry_attr=expiry_attrself._deserializer=TypeDeserializer()super().__init__()

One record exists per circuit name. This is the utility's internal representation;
user code never sees it directly, only the CircuitInfo produced by
:meth:to_circuit_info.

PARAMETER

DESCRIPTION

name

Circuit name, used as the partition key in the store.

Source code in aws_lambda_powertools/utilities/circuit_breaker_alpha/persistence/record.py

474849505152535455565758596061626364

defto_circuit_info(self)->CircuitInfo:""" Project this record to the public ``CircuitInfo`` handed to user code. Strips internal fields (``half_open_owner``, ``expiry_timestamp``) so no persistence detail leaks across the public boundary. Returns ------- CircuitInfo Public snapshot of the circuit. """returnCircuitInfo(name=self.name,state=self.state,failure_count=self.failure_count,opened_at=self.opened_at,)