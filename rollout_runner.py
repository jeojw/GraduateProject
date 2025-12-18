from trajectory_logger import TrajectoryLogger

def run_episode(env, agent1, agent2, max_steps=400):
    logger = TrajectoryLogger()
    obs = {"state": env.reset()}

    for _ in range(max_steps):
        a1 = agent1.act(obs)
        a2 = agent2.act(obs)

        result = env.step((a1, a2))
        obs = result

        logger.log(result["t"], agent1.name, a1, obs["state"], result["reward"])
        logger.log(result["t"], agent2.name, a2, obs["state"], result["reward"])

        if result["done"]:
            break

    return logger.get_events()