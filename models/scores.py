import json

class Score:
    """
    This class handles the scores stored in the scores.json file
    """
    def __init__(self, filename):
        # get the information from the scores.json file
        self.filename = filename
        self.scores = []
        with open(self.filename, 'r') as file:
            user_info = json.load(file)
            for score in user_info:
                self.scores.append(score)
        self.scores = sorted(self.scores, key=lambda rank: rank['score'], reverse=True)
            
    def __len__(self):
        return len(self.scores)
    
    def get_scores(self):
        """
        Return a list of dictionaries with the scores
        """
        return self.scores

    def save(self):
        """
        This method will save the scores to the scores.json file
        """
        with open(self.filename, 'w') as file:
            json.dump(self.scores, file)

