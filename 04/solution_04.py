import numpy as np


def q_learning(env, alpha=0.1, epsilon=0.1, gamma=0.9, max_steps=10000):
   
    S = env.getNumStates()
    A = env.getNumActions()
    Q = np.zeros((S, A))

    steps = 0
    while steps <= max_steps:
        s = env.reset()
        
        done = False
        while not done and steps <= max_steps:
            # epsilon greedy
            if np.random.random() > 1 - epsilon:
                a = np.random.randint(A)  # random action
            else:
                max_Q = np.max(Q[s])
                actions_with_max_Q = np.where(Q[s] == max_Q)[0]
                a = np.random.choice(actions_with_max_Q)  #best action

            r, s_prime, done = env.step(a)
            
            # q table yeniden
            Q[s, a] = Q[s, a] + alpha * (r + gamma * np.max(Q[s_prime]) - Q[s, a])
            s = s_prime
            steps += 1

            
            

    return Q





