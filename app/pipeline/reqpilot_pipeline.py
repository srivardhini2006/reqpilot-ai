from app.agents.executive_summary_agent import ExecutiveSummaryAgent
from app.validators.pipeline_validator import PipelineValidator
from app.agents.traceability_agent import TraceabilityAgent
from app.agents.functional_requirement_agent import FunctionalRequirementAgent
from app.agents.use_case_agent import UseCaseAgent
from app.agents.business_rule_agent import BusinessRuleAgent
from app.agents.data_requirement_agent import DataRequirementAgent
from app.agents.non_functional_requirement_agent import (
    NonFunctionalRequirementAgent
)
from app.agents.fsd_assembly_agent import FSDAssemblyAgent

from app.agents.test_scenario_agent import TestScenarioAgent
from app.agents.test_case_agent import TestCaseAgent
from app.agents.test_traceability_agent import TestTraceabilityAgent


class ReqPilotPipeline:

    def __init__(self):

        self.validator = PipelineValidator()

        self.executive_summary_agent = ExecutiveSummaryAgent()

        self.traceability_agent = TraceabilityAgent()

        self.functional_requirement_agent = (
            FunctionalRequirementAgent()
        )

        self.use_case_agent = UseCaseAgent()
        

        self.business_rule_agent = BusinessRuleAgent()

        self.data_requirement_agent = DataRequirementAgent()

        self.non_functional_requirement_agent = (
            NonFunctionalRequirementAgent()
        )

        self.fsd_assembly_agent = FSDAssemblyAgent()

        self.test_scenario_agent = TestScenarioAgent()

        self.test_case_agent = TestCaseAgent()

        self.test_traceability_agent = TestTraceabilityAgent()

    def run(self, state):

     print("Starting ReqPilot pipeline...")

     print("1. Executive Summary")
     state = self.executive_summary_agent.analyze(state)

     print("2. Functional Requirements")
     state = self.functional_requirement_agent.analyze(state)

     print("3. Use Cases")
     state = self.use_case_agent.analyze(state)

     print("4. Business Rules")
     state = self.business_rule_agent.analyze(state)

     print("5. Data Requirements")
     state = self.data_requirement_agent.analyze(state)

     print("6. Non-Functional Requirements")
     state = self.non_functional_requirement_agent.analyze(state)

     print("7. Requirement Traceability")
     state = self.traceability_agent.analyze(state)

     print("8. FSD Assembly")
     state = self.fsd_assembly_agent.analyze(state)

     print("9. Test Scenarios")
     state = self.test_scenario_agent.analyze(state)

     print("10. Test Cases")
     state = self.test_case_agent.analyze(state)

     print("11. Test Traceability")
     state = self.test_traceability_agent.analyze(state)
     print("12. Pipeline Validation")

     validation_errors = self.validator.validate(state)

     if validation_errors:

      print("Pipeline validation failed.")

      for error in validation_errors:
        print(f"- {error}")

      else:

       print("Pipeline validation passed.")

     print("ReqPilot pipeline completed.")

     return state

     print("ReqPilot pipeline completed.")

     return state
    