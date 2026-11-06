# aws_lambda_powertools.utilities.parser.envelopes.vpc_latticev2 API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/vpc_latticev2.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/vpc_latticev2.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.vpc_latticev2`

## Classes

- `class VpcLatticeV2Envelope`
- 
## Expand source code`class VpcLatticeV2Envelope(BaseEnvelope): """Amazon VPC Lattice envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice V2 model {VpcLatticeV2Model}") parsed_envelope: VpcLatticeV2Model = VpcLatticeV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Amazon VPC Lattice envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice V2 model {VpcLatticeV2Model}") parsed_envelope: VpcLatticeV2Model = VpcLatticeV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Model | None`
- Parsed detail payload with model provided