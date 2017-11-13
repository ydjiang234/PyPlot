class Plot_Operator:

    def  __init__(self):
        return None

    def set_xy_labels(self, ax, x_label, y_label):
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

    def set_xy_lims(self, ax, x_range, y_range):
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)

    def set_x_major_tick(self, ax, major):
        import matplotlib.ticker as ticker
        ax.xaxis.set_major_locator(ticker.MultipleLocator(major))
        
    def set_y_major_tick(self, ax, major):
        import matplotlib.ticker as ticker
        ax.yaxis.set_major_locator(ticker.MultipleLocator(major))

    def set_xy_major_tick(self, ax, major_x, major_y):
        import matplotlib.ticker as ticker
        ax.xaxis.set_major_locator(ticker.MultipleLocator(major_x))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(major_y))

    def add_axis_unit(self, ax, label, axis='x', skip=2):
        if axis == 'x':
            labels = ax.get_xticks().tolist()
            labels = [str(item)[:-1*skip] + label for item in labels]
            ax.set_xticklabels(labels)
        elif axis == 'y':
            labels = ax.get_yticks().tolist()
            labels = [str(item)[:-1*skip] + '%' for item in labels]
            ax.set_yticklabels(labels)

    def analyse_lim_ticks(self, max_value, num, intervals):
        import numpy as np
        nums = np.floor(max_value/intervals) + 1
        diffs = abs(nums-num)
        index = diffs.argmin()
        cur_num = nums[index]
        cur_interval = intervals[index]
        cur_max_value = cur_num * cur_interval
        return cur_interval, cur_max_value

    def auto_lim_tick(self, ax, axis, num, intervals, is_sym=False, extra=1.02):
        import numpy as np
        data_max = np.array([])
        for line in ax.lines:
            if axis == 'x':
                cur_data = line.get_xdata()
            elif axis == 'y':
                cur_data = line.get_ydata()
            data_max = np.append(data_max, max(abs(cur_data)))
        max_value = max(data_max) * extra
            
        cur_interval, cur_max_value = self.analyse_lim_ticks(max_value, num, intervals)
        
        if is_sym:
            range1 = (-cur_max_value, cur_max_value)
        else:
            range1 = (0, cur_max_value)

        if axis == 'x':
            ax.set_xlim(range1)
            self.set_x_major_tick(ax, cur_interval)
        elif axis == 'y':
            ax.set_ylim(range1)
            self.set_y_major_tick(ax, cur_interval)


    def tight(self, fig):
        fig.tight_layout()
