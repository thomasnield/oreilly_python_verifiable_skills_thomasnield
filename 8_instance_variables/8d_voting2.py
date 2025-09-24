class VotingPoll:  
    def __init__(self):  
        self.candidate_A = 0  
        self.candidate_B = 0  
        self.candidate_C = 0
  
    def vote_candidate_A(self):  
        self.candidate_A += 1  
  
    def vote_candidate_B(self):  
        self.candidate_B += 1  
        
    def vote_candidate_C(self):  
        self.candidate_C += 1   
        
voting_poll = VotingPoll()  
  
# give 3 votes to candidate A  
voting_poll.vote_candidate_A()  
voting_poll.vote_candidate_A()  
voting_poll.vote_candidate_A()  
  
# give 2 votes to candidate B  
voting_poll.vote_candidate_B()  
voting_poll.vote_candidate_B()  
  
# give 1 vote to candidate C 
voting_poll.vote_candidate_C()  

print(f"A: {voting_poll.candidate_A}, B: {voting_poll.candidate_B}, C: {voting_poll.candidate_C}")