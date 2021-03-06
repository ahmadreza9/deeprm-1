import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
import os
rnn = True

onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

#if rnn:
work_rnn = [f for f in onlyfiles if f.endswith("_work_complete_rnn.npy")]

work_rnn = zip([f.strip("_work_complete_rnn.npy") for f in work_rnn],
    [np.load(f).item() for f in work_rnn])
#else:
work = [f for f in onlyfiles if f.endswith("_work_complete.npy")]

work = zip([f.strip("_work_complete.npy") for f in work],
               [np.load(f).item() for f in work])

amps =[]
ratios = []
halluc = []
halluc_rnn = []
reg_rnn = []
reg = []

work_rnn = [(int(name.split("_")[0]), amp_sds) for name, amp_sds in work_rnn]

work = [(int(name.split("_")[0]), amp_sds) for name, amp_sds in work]

work_rnn.sort()

work.sort()

for amp, amp_sds in work_rnn:
    print(name)
    r = np.mean([np.mean(s) for s in amp_sds['PG', 'Regular']])
    print r, ": regular"
    h = np.mean([np.mean(s) for s in amp_sds['PG', 'Hallucinated']])
    print h, ": halluc"
    print h / r, ": ratio"

    amps.append(amp)
    halluc_rnn.append(h)
    reg_rnn.append(r)
    ratios.append(h / r)


for amp, amp_sds in work:
    print(name)
    r = np.mean([np.mean(s) for s in amp_sds['PG', 'Regular']])
    print r, ": regular"
    h = np.mean([np.mean(s) for s in amp_sds['PG', 'Hallucinated']])
    print h, ": halluc"
    print h / r, ": ratio"

    #amps.append(amp)
    halluc.append(h)
    reg.append(r)
    ratios.append(h / r)

print(ratios)
print(amps)

plt.figure()
plt.plot(amps, reg, amps, halluc, amps, reg_rnn, amps, halluc_rnn, linewidth=2)
plt.legend(['FFN (GT)', 'FFN + Ground Truth SFP', 'FFN (RNN)', 'FFN + RNN SFP'])
plt.xlabel('Max Job Duration')
plt.ylabel('Mean Work Complete')
plt.show()


'''
sd4 = np.load(slowdowns[3])
sd6 = np.load(slowdowns[4])
sd8 = np.load(slowdowns[5])
sd10 = np.load(slowdowns[0])
sd12 = np.load(slowdowns[1])
sd14 = np.load(slowdowns[2])

jobs_work_complete = np.load('jobs_work_complete.npy').item()
#-- matplotlib colormap no overlap --
plot = True
if plot:
    traj_types = ["Regular", "Hallucinated"]
    num_colors = len(traj_types)
    cm = plt.get_cmap('gist_rainbow')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_color_cycle([cm(1. * i / num_colors) for i in range(num_colors)])

    for test_type in ['PG']:
        for traj_type in traj_types:
            work_complete_cdf = np.sort(np.concatenate(jobs_work_complete[test_type, traj_type]))
            work_complete_yvals = np.arange(len(work_complete_cdf))/float(len(work_complete_cdf))
            ax.plot(work_complete_cdf, work_complete_yvals, linewidth=2, label=traj_type)

    plt.legend(loc=4)
    plt.xlabel("job slowdown", fontsize=20)
    plt.ylabel("CDF", fontsize=20)
    # plt.show()
    plt.savefig("blah_slowdown_fig" + ".pdf")
'''