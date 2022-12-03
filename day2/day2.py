shapes_scores_dict = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3} # A for Rock, B for Paper, and C for Scissors
game_outcome_scores_dict = {'lost':0, 'tie':3, 'win':6}
my_winning_shape = {'A':'Y', 'B':'Z', 'C':'X'}
my_loosing_shape = {'A':'Z', 'B':'X', 'C':'Y'}


def part1():
    with open('data.txt', 'r') as f:
        final_score = 0
        for line in f:
            shape_opponent, shape_mine = line.strip().split(' ')
            
            if shapes_scores_dict[shape_opponent] == shapes_scores_dict[shape_mine]: # tie
                game_score = game_outcome_scores_dict['tie'] + shapes_scores_dict[shape_mine]
            elif shape_mine == my_winning_shape[shape_opponent]: # I won
                game_score = game_outcome_scores_dict['win'] + shapes_scores_dict[shape_mine]
            else: # I lost
                game_score = shapes_scores_dict[shape_mine]
            
            final_score += game_score
        
        print(final_score)
    

def part2():
    game_outcome_scores_dict = {'X':0, 'Y':3, 'Z':6}

    with open('data.txt', 'r') as f:
        final_score = 0
        for line in f:
            shape_opponent, game_outcome = line.strip().split(' ')
            if game_outcome == 'X': # lost
                game_score = game_outcome_scores_dict[game_outcome] + shapes_scores_dict[my_loosing_shape[shape_opponent]]
            elif game_outcome == 'Y': # tie
                game_score = game_outcome_scores_dict[game_outcome] + shapes_scores_dict[shape_opponent]
            else: # win
                game_score = game_outcome_scores_dict[game_outcome] + shapes_scores_dict[my_winning_shape[shape_opponent]]
            
            final_score += game_score
        
        print(final_score)


if __name__ == "__main__":
    part1()
    part2()