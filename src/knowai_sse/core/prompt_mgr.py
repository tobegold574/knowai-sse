from typing import Dict

from ..exceptions import PromptBuildError


class PromptManager:
    VALUE_DESCRIPTORS = {
        "radical": "侧重前沿实验室、GitHub 趋势、未发表论文、突破性技术",
        "ethics": "关注 AI 伦理、数字鸿沟、技术公平性、社会影响",
        "practical": "关注工程实践、应用案例、落地效果、商业价值",
        "academic": "侧重理论基础、学术严谨性、同行评审、引用分析",
        "open_source": "关注开源项目、社区生态、开发者工具、协作模式"
    }

    def __init__(self) -> None:
        self.base_system_prompt = (
            "你是一个专业的搜索意图发散助手。"
            "你的任务是根据给定的核心主题和价值观权重，"
            "生成一组高质量的搜索指令。\n\n"
            "请严格按照以下 JSON 格式返回结果：\n"
            "{\n"
            '  "instructions": [\n'
            '    {\n'
            '      "channel": "arxiv|web|rss",\n'
            '      "query": "搜索查询语句",\n'
            '      "time_range": "时间范围（如：latest, past_24h, past_week）"\n'
            "    }\n"
            "  ]\n"
            "}\n\n"
            "注意事项：\n"
            "1. channel 必须是 \"arxiv\"、\"web\" 或 \"rss\" 之一\n"
            "2. arxiv 查询应使用 LaTeX 语法或 arXiv 搜索语法\n"
            "3. web 查询可使用 Google Search Operators（如 filetype:pdf, site:edu）\n"
            "4. time_range 建议使用 \"latest\"、\"past_24h\"、\"past_week\" 或 \"past_month\"\n"
            "5. 生成 5-10 条搜索指令，覆盖不同维度"
        )

    def build_system_prompt(self, values_map: Dict[str, float]) -> str:
        try:
            value_constraints = []

            for value, weight in values_map.items():
                if value in self.VALUE_DESCRIPTORS:
                    constraint = (
                        f"- {value} (权重: {weight}): "
                        f"{self.VALUE_DESCRIPTORS[value]}"
                    )
                    value_constraints.append(constraint)

            if value_constraints:
                constraints_section = "\n".join(value_constraints)
                enhanced_prompt = (
                    f"{self.base_system_prompt}\n\n"
                    f"价值观约束：\n{constraints_section}"
                )
            else:
                enhanced_prompt = self.base_system_prompt

            return enhanced_prompt
        except Exception as e:
            raise PromptBuildError(f"构建系统提示词失败: {e}")

    def build_user_prompt(self, theme: str) -> str:
        return f"""核心主题：{theme}

请根据上述价值观约束，围绕这个核心主题生成一组搜索指令。"""

    def build_prompts(self, theme: str, values_map: Dict[str, float]) -> tuple[str, str]:
        system_prompt = self.build_system_prompt(values_map)
        user_prompt = self.build_user_prompt(theme)
        return system_prompt, user_prompt
