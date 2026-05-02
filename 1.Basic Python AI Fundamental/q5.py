class SimpleAIAgent:
    def perceive(self, environment):
        return environment

    def act(self, perception):
        # Simple decision rules
        if perception == "hungry":
            return "Eat food"
        elif perception == "tired":
            return "Take rest"
        elif perception == "study time":
            return "Start studying"
        elif perception == "thirsty":
            return "Drink water"
        else:
            return "Do nothing"

# Create agent
agent = SimpleAIAgent()

# Simulated environment inputs
environments = ["hungry", "tired", "study time", "thirsty", "idle"]

# Run agent
for env in environments:
    perception = agent.perceive(env)
    action = agent.act(perception)
    print(f"Environment: {env} → Action: {action}")
