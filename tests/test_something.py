#test
"""
file:
    create_trimmed_model

test parameter:
    number and name of species eliminated

"""

#import function
from create_trimmed_model import create_trimmed_model as test_func

#define function inputs
data_file=('gri30.xml')
exclusion_list = ['02', 'CO2']



#call Function
test_func(data_file, exclusion_list)

#print species number
print(initial_solution.n_reactions)
print(new_solution.n_reactions)


def test_answer():
    assert func(3) == 5
