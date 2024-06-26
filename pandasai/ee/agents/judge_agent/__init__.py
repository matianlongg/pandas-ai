'''
Author: mtl131 576694002@qq.com
Date: 2024-06-19 09:02:47
LastEditors: mtl131 576694002@qq.com
LastEditTime: 2024-06-19 14:27:16
FilePath: /server/home/aiuser/miniconda3/envs/gbi/lib/python3.11/site-packages/pandasai/ee/agents/judge_agent/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import Optional, Union

from pandasai.agent.base_judge import BaseJudge
from pandasai.config import load_config_from_json
from pandasai.ee.agents.judge_agent.pipeline.judge_pipeline import JudgePipeline
from pandasai.pipelines.abstract_pipeline import AbstractPipeline
from pandasai.pipelines.judge.judge_pipeline_input import JudgePipelineInput
from pandasai.pipelines.pipeline_context import PipelineContext
from pandasai.schemas.df_config import Config


class JudgeAgent(BaseJudge):
    def __init__(
        self,
        config: Optional[Union[Config, dict]] = None,
        pipeline: AbstractPipeline = None,
    ) -> None:
        context = None
        if config:
            if isinstance(config, dict):
                config = Config(**load_config_from_json(config))

            context = PipelineContext(None, config)

        pipeline = pipeline or JudgePipeline(context=context)
        super().__init__(pipeline)

    def evaluate(self, query: str, code: str) -> bool:
        input_data = JudgePipelineInput(query, code)
        return self.pipeline.run(input_data)
