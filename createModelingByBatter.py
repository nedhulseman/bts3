#-- Base packages
import os
import sys

#-- Pypi packages
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)

#-- Custom packages

#-- Functions
def get_modeling_data():
    game_lvl = pd.read_csv('./data/GameLvl.csv')
    game_lvl['PAs'] = game_lvl['hits'] + game_lvl['outs'] + game_lvl['non_abs']
    game_lvl['ABs'] = game_lvl['hits'] + game_lvl['outs']
    game_lvl['hit_ind'] = np.where( game_lvl['hits'] > 0, 1,0)



    rp_batter = pd.read_csv('./data/RPBatter.csv')
    ytd_batter = pd.read_csv('./data/YTDBatter.csv')
    rename_cols = {
        'rp_hits': 'ytd_hits',
        'rp_outs': 'ytd_outs',
        'rp_non_abs': 'ytd_non_abs',
        'rp_hits_var': 'ytd_hits_var',
        'rp_games_played': 'ytd_games_played',
    }
    keep_cols = ['game_pk', 'batter'] + list(rename_cols.values())
    ytd_batter = ytd_batter.rename(columns=rename_cols)
    ytd_batter = ytd_batter[keep_cols]
    game_lvl = pd.merge(game_lvl, ytd_batter, how='left', on=['game_pk', 'batter'])
    game_lvl['ytd_PAs'] = game_lvl['ytd_hits'] + game_lvl['ytd_non_abs'] + game_lvl['ytd_outs']
    game_lvl['ytd_ABs'] = game_lvl['ytd_hits'] + game_lvl['ytd_outs']
    game_lvl['ytd_AB_div_PA'] = (game_lvl['ytd_ABs'] / game_lvl['ytd_PAs']).round(3)
    game_lvl['ytd_BA'] = (game_lvl['ytd_hits'] / game_lvl['ytd_ABs']).round(3)

    rp_sp = pd.read_csv('./data/RPPitcher.csv')
    rename_cols = {
        'rp_hits': 'rp_hits_sp',
        'rp_outs': 'rp_outs_sp',
        'rp_non_abs': 'rp_non_abs_sp',
        'rp_games_played': 'rp_games_played_sp',
        'rp_hits_var': 'rp_hits_var_sp',
        'pitcher': 'starting_pitcher'
    }
    keep_cols = ['game_pk'] + list(rename_cols.values())
    rp_sp = rp_sp.rename(columns=rename_cols)
    rp_sp = rp_sp[keep_cols]
    game_lvl = pd.merge(game_lvl, rp_sp, how='left', on=['game_pk', 'starting_pitcher'])
    game_lvl['rp_PAs_sp'] = game_lvl['rp_hits_sp'] + game_lvl['rp_outs_sp'] + game_lvl['rp_non_abs_sp']
    game_lvl['rp_ABs_sp'] = game_lvl['rp_hits_sp'] + game_lvl['rp_outs_sp']
    game_lvl['rp_AB_div_PA_sp'] = (game_lvl['rp_ABs_sp'] / game_lvl['rp_PAs_sp']).round(3)
    game_lvl['rp_BA_sp'] = (game_lvl['rp_hits_sp'] / game_lvl['rp_ABs_sp']).round(3)

    ytd_sp = pd.read_csv('./data/YTDPitcher.csv')
    rename_cols = {
        'rp_hits': 'ytd_hits_sp',
        'rp_outs': 'ytd_outs_sp',
        'rp_non_abs': 'ytd_non_abs_sp',
        'rp_games_played': 'ytd_games_played_sp',
        'rp_hits_var': 'ytd_hits_var_sp',
        'pitcher': 'starting_pitcher'
    }
    keep_cols = ['game_pk'] + list(rename_cols.values())
    ytd_sp = ytd_sp.rename(columns=rename_cols)
    ytd_sp = ytd_sp[keep_cols]
    game_lvl = pd.merge(game_lvl, ytd_sp, how='left', on=['game_pk', 'starting_pitcher'])
    game_lvl['ytd_PAs_sp'] = game_lvl['ytd_hits_sp'] + game_lvl['ytd_outs_sp'] + game_lvl['ytd_non_abs_sp']
    game_lvl['ytd_ABs_sp'] = game_lvl['ytd_hits_sp'] + game_lvl['ytd_outs_sp']
    game_lvl['ytd_AB_div_PA_sp'] = (game_lvl['ytd_ABs_sp'] / game_lvl['ytd_PAs_sp']).round(3)
    game_lvl['ytd_BA_sp'] = (game_lvl['ytd_hits_sp'] / game_lvl['ytd_ABs_sp']).round(3)




    #-- deprecated
    #game_lvl['rp_end_date'] = game_lvl.apply(lambda x: rp_batter.loc[(rp_batter['batter']== x['batter']) & (rp_batter['game_date']<x['game_date']), 'game_date'].max(), axis=1)



    game_lvl = pd.merge(game_lvl, rp_batter, how='left', on=['game_pk', 'batter'])
    game_lvl['rp_PAs'] = game_lvl['rp_hits'] + game_lvl['rp_non_abs'] + game_lvl['rp_outs']
    game_lvl['rp_ABs'] = game_lvl['rp_hits'] + game_lvl['rp_outs']
    game_lvl['rp_AB_div_PA'] = (game_lvl['rp_ABs'] / game_lvl['rp_PAs']).round(3)
    game_lvl['rp_BA'] = (game_lvl['rp_hits'] / game_lvl['rp_ABs']).round(3)

    matchups = pd.read_csv('./data/matchups.csv')
    matchups['match_year_PAs'] = matchups['year_hits']+matchups['year_outs']+matchups['year_non_abs']
    matchups['match_year_ABs'] = matchups['year_hits']+matchups['year_outs']
    matchups['match_year_BA'] =  (matchups['year_hits'] / matchups['match_year_ABs']).round(3)
    matchups['match_year_AB_div_PA'] = (matchups['match_year_ABs'] / matchups['match_year_PAs']).round(3)
    matchups['match_career_PAs'] = matchups['career_hits']+matchups['career_outs']+matchups['career_non_abs']
    matchups['match_career_ABs'] = matchups['career_hits']+matchups['career_outs']
    matchups['match_career_BA'] =  (matchups['career_hits'] / matchups['match_career_ABs']).round(3)
    matchups['match_career_AB_div_PA'] = (matchups['match_career_ABs'] / matchups['match_career_PAs']).round(3)
    keep_cols = ['match_year_PAs', 'match_year_BA', 'match_year_AB_div_PA',
                'match_career_PAs', 'match_career_BA', 'match_career_AB_div_PA',
                'batter', 'pitcher', 'game_pk'
    ]
    matchups = matchups[keep_cols]
    left_on = ['batter', 'starting_pitcher', 'game_pk']
    right_on = ['batter', 'pitcher', 'game_pk']
    matchups = matchups.fillna(0)
    game_lvl = pd.merge(game_lvl, matchups, how='left', left_on=left_on, right_on=right_on)

    player_meta = pd.read_csv('./data/player_meta.csv')
    player_meta = player_meta.loc[player_meta['pos']=='pitcher', ['player', 'p_throws']].drop_duplicates()
    game_lvl = pd.merge(game_lvl, player_meta, left_on='starting_pitcher', right_on='player')
    game_lvl['handedness_matchup'] = game_lvl['stand'] +'-'+ game_lvl['p_throws']
    game_lvl = game_lvl.loc[game_lvl['rp_PAs'] > 20]
    game_lvl = game_lvl.rename(columns={'game_date_x':'game_date'})
    modeling_vars = [
        'rp_BA', 'rp_AB_div_PA', 'ytd_BA', 'ytd_AB_div_PA', 'rp_hits_var', 'ytd_hits_var',
        'inning_topbot', 'handedness_matchup', 'hit_ind',
        'rp_BA_sp', 'rp_AB_div_PA_sp', 'ytd_BA_sp', 'ytd_AB_div_PA_sp',
        'match_year_PAs', 'match_year_BA', 'match_year_AB_div_PA',
        'match_career_PAs', 'match_career_BA', 'match_career_AB_div_PA'
    ]
    id_vars = ['game_date', 'game_pk', 'batter', 'starting_pitcher', 'ABs', 'hits']
    dummy_vars = ['inning_topbot', 'handedness_matchup']
    game_lvl = game_lvl[modeling_vars + id_vars]
    game_lvl = pd.get_dummies(game_lvl, columns=dummy_vars, prefix ='', prefix_sep = '')

    game_lvl.to_csv('./data/modeling_data.csv', index=False)

    modeling_data = pd.read_csv('./data/modeling_data.csv').dropna()
    print("modeling_data shape: ", str(modeling_data.shape))

    modeling_data['ytd_BA_x_var'] = modeling_data['ytd_BA'] * modeling_data['ytd_hits_var']
    modeling_data['rp_BA_x_var'] = modeling_data['rp_BA'] * modeling_data['rp_hits_var']

    pd_id = modeling_data.drop_duplicates(subset='batter')
    pd_id = pd_id[['batter']]
    pd_id.shape

    np.random.seed(57)
    pd_id['wookie'] = (np.random.randint(0,10000,pd_id.shape[0]))/10000

    pd_id = pd_id[['batter', 'wookie']]

    pd_id['MODELING_GROUP'] = np.where(((pd_id.wookie <= .75)), 'TRAINING', 'TEST')

    players_per_group = pd_id.groupby(['MODELING_GROUP'])['wookie'].count()
    players_per_group

    modeling_data = modeling_data.sort_values(by=['batter'], ascending = [True])
    pd_id = pd_id.sort_values(by=['batter'], ascending = [True])

    modeling_data = modeling_data.merge(pd_id, on=['batter'], how='inner')

    train = modeling_data[modeling_data['MODELING_GROUP']=='TRAINING']
    test = modeling_data[modeling_data['MODELING_GROUP']=='TEST']
    

    return None
