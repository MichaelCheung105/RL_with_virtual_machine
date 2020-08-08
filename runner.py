from environment import Environment
from agent import Agent
from sql_database import SqlDB


class Runner:
    def __init__(self, env: Environment, agent: Agent, external_storage: SqlDB):
        # Initiate Environment and Agent
        self.env = env
        self.agent = agent
        self.experience_pool = external_storage

    def start(self):
        state = self.env.init_state()
        total_episode = 100
        for train_episode in range(total_episode):
            # Interact with environment
            action = self.agent.get_action(state)
            reward, next_state, done = self.env.step(action)

            # Store experiences
            experience = list(state) + [action, reward] + list(next_state) + [int(done)]
            self.experience_pool.insert_experience(table_name='exp_pool_1', experience_tuple=tuple(experience))

            # Update agent and state
            self.agent.update_model(train_episode, total_episode)
            state = next_state


if __name__ == "__main__":
    # Initiate objects
    env = Environment()
    agent = Agent()
    external_storage = SqlDB()

    # Initiate Experience Pool
    experience_pool_name = "exp_pool_1"
    state_info = {'s1': {'data_type': 'numeric', 'constraint': 'NULL'},
                  's2': {'data_type': 'numeric', 'constraint': 'NULL'},
                  's3': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'a': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'r': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'sp1': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'sp2': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'sp3': {'data_type': 'numeric', 'constraint': 'NULL'},
                  'd': {'data_type': 'numeric', 'constraint': 'NULL'}
                  }
    external_storage.create_table_as_experience_pool(table_name=experience_pool_name,
                                                     table_cols=state_info,
                                                     is_overwrite=True)

    runner = Runner(env=env, agent=agent, external_storage=external_storage)
    runner.start()
    # Notice trainer that training is completed
    print("Training Completed!!! Goodbye")
