import matplotlib.pyplot as plt

aggregate_dimension = 'timestep'
run_count = 10
time_step_count = 1040

def dist_plot(_df, x, y,lx=False,ly=False, suppMin=False):       
    '''
    Generates Monte Carlo plot of mean, median, mean + 1 sd. Option to plot either mean-1 sd or minimum.
    Option to plot log-scale on x or y.
    '''
    mean_df = _df.groupby(aggregate_dimension).mean().reset_index()
    median_df = _df.groupby(aggregate_dimension).median().reset_index()
    std_df = _df.groupby(aggregate_dimension).std().reset_index()
    min_df = _df.groupby(aggregate_dimension).min().reset_index()

    plt.figure(figsize=(10,6))
    if not(suppMin):
        plt.plot(mean_df[x].values, mean_df[y].values,
             mean_df[x].values,median_df[y].values,
             mean_df[x].values,mean_df[y].values+std_df[y].values,
             mean_df[x].values,min_df[y].values)
        plt.legend(['mean', 'median', 'mean + 1*std', 'min'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        
    else:
        plt.plot(mean_df[x].values, mean_df[y].values,
             mean_df[x].values,median_df[y].values,
             mean_df[x].values,mean_df[y].values+std_df[y].values,
             mean_df[x].values,mean_df[y].values-std_df[y].values)
        plt.legend(['mean', 'median', 'mean + 1*std', 'mean - 1*std'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.xlabel(x)
    plt.ylabel(y)
    if lx:
        plt.xscale('log')
    
    if ly:
        plt.yscale('log')

def first_five_plot(_df, state_var):
    '''
    Enter state variable name as a string. Generates timeseries plot of at most the first five
    Monte Carlo runs along with the mean of ALL runs. Use run_count variable name for number of runs.
    '''
    mean_df = _df.groupby(aggregate_dimension).mean().reset_index()
    plt.figure(figsize=(10,6))
    if run_count < 5:
        runs = run_count
    else:
        runs = 5
    for r in range(1,runs+1):
        legend_name = 'Run ' + str(r)
        plt.plot(_df[_df.run==r].timestep, _df[_df.run==r][state_var], label = legend_name )
    plt.plot(mean_df.timestep, mean_df[state_var], label = 'Mean', color = 'black')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('Timestep')
    plt.ylabel(state_var)
    title_text = 'Performance of ' + state_var + ' over the First ' + str(runs) + ' Monte Carlo Runs'
    plt.title(title_text)

def overview_plot(mech_steps, *args, **kwargs):
    '''
    *args, enter df fields of desired plots
    uses time_step_count and run_count variable name from simulation runs.
    **kwarg y_label for custom y axis title
    **kwarg legend_label for custom legend label
    '''
    plt.figure(figsize=(10,6))
    for r in range(run_count):
        plt.axvline(x= mech_steps * time_step_count * r, color ='b')
    for arg in args:
        for key, value in kwargs.items():
            if key == 'y_label':
                plt.ylabel(value)
            if key == 'legend_label':
                plt.plot(arg, label = value)
            else:
                plt.plot(arg) #, label = arg.in
#         plt.plot(arg, label = y_label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    x_text = 'Timestep Repeated over ' + str(run_count) + ' Runs'
    plt.xlabel(x_text)
    plt.title('Overview of Repeated Monte Carlo Runs')
