import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

utils = importr("utils")
utils.chooseCRANmirror(graphics=False, ind=1)

def InstallFitzRoy():
    install = utils.install_packages
    install("fitzRoy")
    fitzroy = importr("fitzRoy")
    return fitzroy

fitzroy = InstallFitzRoy()

def RunStats(ids_start, ids_end):
    matches = robjects.r.seq(ids_start, ids_end)
    player_stats = fitzroy.get_footywire_stats(ids=matches)
    utils.write_csv(player_stats, "Data_Files/player_stats.csv")