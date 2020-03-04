import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

utils = importr("utils")
install = utils.install_packages

install("fitzRoy")
fitzroy = importr("fitzRoy")

matches = robjects.r.seq(9514, 9927)
player_stats = fitzroy.get_footywire_stats(ids=matches)

utils.write_csv(player_stats, "Data_Files/player_stats_2018_2019.csv")