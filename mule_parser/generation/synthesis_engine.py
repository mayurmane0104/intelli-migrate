from typing import List
from mule_parser.models.semantic_graph import SemanticNode
from mule_parser.dataweave.dw_complexity_analyzer import DWComplexityAnalyzer, TransformationStrategy
from mule_parser.generation.imperative_generator import DWImperativeGenerator
from mule_parser.generation.template_generator import DWTemplateGenerator

class SynthesisEngine:
    def __init__(self):
        self.analyzer = DWComplexityAnalyzer()
        self.imperative_gen = DWImperativeGenerator()
        self.template_gen = DWTemplateGenerator()

    def synthesize(self, root_nodes: List[SemanticNode]) -> dict:
        strategy = self.analyzer.analyze(root_nodes)
        
        if strategy == TransformationStrategy.IMPERATIVE_SYNTHESIS:
            code = self.imperative_gen.generate(root_nodes)
            nodes_used = self.imperative_gen.generated_nodes_count
        else:
            code = self.template_gen.generate(root_nodes)
            nodes_used = self.template_gen.generated_nodes_count
            
        return {
            "strategy": strategy.value,
            "code": code,
            "generated_nodes_count": nodes_used
        }
