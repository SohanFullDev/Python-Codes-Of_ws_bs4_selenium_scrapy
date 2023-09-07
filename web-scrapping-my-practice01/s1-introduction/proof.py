
import pandas as pd
states = ["California","Texas","Florida","New York"];
population = [396123394, 29730311, 21944577, 19299981];

dict_states = {'States': states, 'Population': population};

df_states = pd.DataFrame.from_dict(dict_states);
print(df_states);












