import importlib
import sys
import os

class ImportValidator:
    def validate_import(self, module_name: str, search_path: str = None) -> bool:
        original_path = list(sys.path)
        try:
            if search_path and search_path not in sys.path:
                sys.path.insert(0, search_path)
            
            importlib.invalidate_caches()
            importlib.import_module(module_name)
            return True
        except ImportError as e:
            print(f"ImportError importing {module_name}: {e}", file=sys.stderr)
            return False
        finally:
            sys.path = original_path
