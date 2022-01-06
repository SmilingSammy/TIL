# David Silver RL Course - Lecture1

David Silver 교수님의 RL Course 강의 내용 정리<br>
Lecture 1: Introduction to Reinforcement Learning
- [Lecture](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZBiG_XpjnPrSNw-1XQaM_gB)
- [Lecture Note](https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf)
- [Lecture Note ALL](https://www.davidsilver.uk/teaching/)
- [팡요랩](https://www.youtube.com/watch?v=wYgyiCEkwC8)

## Machine Learning paradigms
![ML Paradigms](ml_paradigms.png)

### Difference between 'RL' and 'SL, UL'
- No supervisor, only a reward signal
- Feedback is delayed by many steps
- Time really matters (Sequential and non-iid data)
- Agent's actions affect the subsequent data

### Example of RL
- Fly stunt manoeuvres in a helicopter
- Defeat the world champion at Backgammon Manage an investment portfolio
- Control a power station
- Make a humanoid robot walk
- Play many different Atari games better than humans

## Rewards
- $$R_t$$ Scalar feedback signal 


## Agent, Environment
- Agent
![agent and environment interation](agent_and_env.png)
  
- Policy
    - agent's behavior
    
- Value Function
    - prediction of future award
    - evaluate the goodness/badness of states
    
- Model
    - predicts what the environment will do next

- RL Agents
    - Value Based
        - value function
    - Policy Based
        - policy
    - actor critic
        - policy
        - value function
    
- Model Free
    - policy and/or value function
- Model Based
    - policy and/or value function
    - Model
    
- 2 Fundamental problems in sequentail decision making
    - RL
        - the environment is initially unknown
        - agent interacts with the environment
        - agent improves its policy
    - planning
        - model of the environment is knwon
        - agent performs computations with its model
        - agent improves its policy
    
- Exploration: finds more information about the environment

