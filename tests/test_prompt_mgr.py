from knowai_sse.core.prompt_mgr import PromptManager


class TestPromptManager:

    def test_build_prompts(self):
        mgr = PromptManager()
        system_prompt, user_prompt = mgr.build_prompts("机器学习", {"academic": 0.9})
        assert "机器学习" in user_prompt
        assert "academic" in system_prompt
        assert "0.9" in system_prompt

    def test_build_prompts_empty_values(self):
        mgr = PromptManager()
        system_prompt, user_prompt = mgr.build_prompts("AI", {})
        assert "AI" in user_prompt
        assert "JSON 格式" in system_prompt
