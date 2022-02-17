
"""
... Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. 
... Store them in a list and find the score of the runner-up.

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score_list = list(arr)
    
    
    def find_min_score(score_list):
        
        min_score = 0
        
        for score in score_list:
            if score < min_score:
                min_score = score
        
        return min_score
             
    def find_max_score(score_list):
        
        max_score = find_min_score(score_list)
        
        for score in score_list:
            if score > max_score:
                max_score = score
                
        return max_score        
                       
    def find_runner_up_score(score_list):
        
        runner_up_score = find_min_score(score_list)
        max_score = find_max_score(score_list)
          
        for score in score_list:
            if score >= runner_up_score and score < max_score:
                runner_up_score = score
                
        return runner_up_score                                            
    print(find_runner_up_score(score_list))        