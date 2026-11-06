from test_export_pipeline_v3 import sample_ir, sample_plan, sample_project_files
def test_dummy(sample_ir, sample_plan, sample_project_files):
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator, ExportValidationError
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import ValidationGenerator
    
    orig_generate = ValidationGenerator.generate
    def patched_generate(self, metadata, vfs):
        print("\n=== VFS PATHS DUMP ===")
        import pprint
        pprint.pprint(vfs.list_paths())
        print("======================\n")
        return orig_generate(self, metadata, vfs)
    ValidationGenerator.generate = patched_generate
    
    orchestrator = ExportOrchestrator()
    try:
        orchestrator.run(
            project_name='AcmeSales',
            target_runtime='python',
            target_format='zip',
            ir=sample_ir,
            migration_plan=sample_plan,
            project_files=sample_project_files,
            infra_mode='sam'
        )
    except ExportValidationError:
        pass
