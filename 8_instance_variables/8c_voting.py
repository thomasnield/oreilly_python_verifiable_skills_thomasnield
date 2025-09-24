class VotingPoll:  
    def __init__(self):  
        self.candidate_A = 0  
        self.candidate_B = 0  
  
voting_poll = VotingPoll()  
  
# oof! This shouldn't be out here! 
voting_poll.candidate_C = 0   

# give 3 votes to candidate A  
voting_poll.candidate_A += 1  
voting_poll.candidate_A += 1  
voting_poll.candidate_A += 1  
  
# give 2 votes to candidate B  
voting_poll.candidate_B += 1  
voting_poll.candidate_B += 1   

# give 1 vote to candidate C  
voting_poll.candidate_C += 1   

print(f"A: {voting_poll.candidate_A}, B: {voting_poll.candidate_B}, C: {voting_poll.candidate_C}")