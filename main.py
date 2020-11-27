import itertools
def dictComp(stop, step):
  # using normal loops to dict
  # dict_comp = {}
  # for n in range(1,stop,step):
  #   key_counter += 1
  #   if (stop - n) >= step:
  #     dict_comp.update({'team-'+str(key_counter): [n+i for i in range(step)]})

  # using comprehension to create dict
  key_counter = itertools.count(1).__next__
 
  dict_comp = {'team-'+str(key_counter()): [n+i for i in range(step)] for n in range(1,stop,step)  if (stop-n) >= step  }
  print(f'{dict_comp}')

dictComp(10,4)