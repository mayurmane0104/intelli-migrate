# aws_lambda_powertools.utilities.parser.envelopes.vpc_lattice API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/vpc_lattice.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/vpc_lattice.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.vpc_lattice`

## Classes

- `class VpcLatticeEnvelope`
- 
## Expand source code`class VpcLatticeEnvelope(BaseEnvelope): """Amazon VPC Lattice envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice model {VpcLatticeModel}") parsed_envelope: VpcLatticeModel = VpcLatticeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Amazon VPC Lattice envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice model {VpcLatticeModel}") parsed_envelope: VpcLatticeModel = VpcLatticeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Model | None`
- Parsed detail payload with model provided