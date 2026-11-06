# Intentionally bridging with FixtureValidationEngine to keep module count matched with spec.
# Runtime equivalence logic is handled in fixture_validation_engine to share dependencies safely.
from mule_parser.verification.fixture_validation_engine import RuntimeEquivalenceValidator
