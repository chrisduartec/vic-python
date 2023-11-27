import pandas as pd
import numpy as np

# Generate ids
ids = np.arange(1, 101)

# Generate defaults
defs = np.random.randint(2, size = 100)

# Generate groups
groups = np.random.randint(low = 1, high = 5, size = 100)

# Create data frame
df = pd.DataFrame(
    {
        "ids": ids,
        "defs": defs,
        "groups": groups
    }
)

# Calculate the PD by group
count_groups = \
    df\
    .groupby('groups', as_index = False)\
    .agg({'defs': 'sum',
          'ids': 'count'})

count_groups['pd'] = count_groups['defs']/count_groups['ids']

# Recent portfolio
ids_rp = np.arange(101, 151)
groups_rp = np.random.randint(low = 1, high = 5, size = 50)

df_rp = pd.DataFrame(
    {
        "ids": ids_rp,
        "groups": groups_rp
    }
)

count_groups_rp = \
    df_rp\
    .groupby('groups', as_index = False)\
    .agg({'ids': 'count'})

count_groups_rp['total'] = len(df_rp)
count_groups_rp['share'] = count_groups_rp['ids']/count_groups_rp['total']

# Create final data frame to calculate weighted average PD
df_final = \
    pd.merge(count_groups, count_groups_rp[['groups', 'share']], on = 'groups', by = 'left')