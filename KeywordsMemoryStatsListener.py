import os 
import webbrowser
import psutil
import datetime

class KeywordsMemoryStatsListener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):

        live_logs_file = open('KeywordsMemoryStatsListener.html','w')

        message = """
        <html>
            <title>Live Memory Stats</title>
            <meta http-equiv="refresh" content="100">
            <link href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css" rel="stylesheet" />
            <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet" />
            <script src="https://code.jquery.com/jquery-3.3.1.js" type="text/javascript"></script>
            <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js" type="text/javascript"></script>
            <script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js" type="text/javascript"></script>
            <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.flash.min.js" type="text/javascript"></script>
            <script>$(document).ready(function() {$('#live').DataTable({"order": [[0, "desc"]]});});</script>
        </html>

        <body>
            <h3 style="color:#009688;text-align:center"><b>RF Live CPU Stats</b></h3>
            <table id="live" class="table table-striped table-bordered">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Suite (Tests)</th>
                        <th>Test Name</th>
                        <th>Keyword Name</th>
                        <th>Stats Before</th>
                        <th>Stats After</th>
                    </tr>
                </thead>
                <tbody>
        """

        live_logs_file.write(message)
        live_logs_file.close()

        current_dir = os.getcwd()
        filename =  current_dir + '/KeywordsMemoryStatsListener.html'

        webbrowser.open_new_tab(filename)

    def start_suite(self, name, attrs):
        self.suite_name = name
        self.test_count = len(attrs['tests'])
    
    def start_test(self, name, attrs):
        self.test_name = name
        if self.test_count != 0:
            self.statsBefore = get_cpu_and_memory_usage_stats()
    
    def start_keyword(self, name, attrs):
        if self.test_count != 0:
            self.statsKBefore = get_cpu_and_memory_usage_stats()
            self.keyword_start_time = get_current_date_time('%Y-%m-%d %H:%M:%S:%f',True)

    def end_keyword(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('KeywordsMemoryStatsListener.html','a+')
            self.statsKAfter = get_cpu_and_memory_usage_stats()

            message = """
                    <tr>
                        <td style="text-align: left;">%s</td>
                        <td style="text-align: left;max-width:300px;background-color:#FFFAFA">%s</td>
                        <td style="text-align: left;max-width:300px;background-color:#FFFAFA">%s</td>
                        <td style="text-align: left;max-width:300px;background-color:#FFFAFA">%s</td>
                        <td style="text-align: left;max-width:300px;background-color:#FFFAFA">%s</td>
                        <td style="text-align: left;max-width:300px;background-color:#FFFAFA">%s</td>
                    </tr>

            """ %(str(self.keyword_start_time), str(self.suite_name), str(self.test_name), str(attrs['kwname']), str(self.statsKBefore), str(self.statsKAfter))

            live_logs_file.write(message)
            live_logs_file.close()
    
    def end_test(self, name, attrs):
        if self.test_count != 0:
            live_logs_file = open('KeywordsMemoryStatsListener.html','a+')
            self.test_end_time = get_current_date_time('%Y-%m-%d %H:%M:%S:%f',True)
            self.statsAfter = get_cpu_and_memory_usage_stats()

            message = """
                
                    <tr>
                        <td style="text-align: left;">%s</td>
                        <td style="text-align: left;max-width:300px;">%s</td>
                        <td style="text-align: left;max-width:300px;">%s</td>
                        <td style="max-width:300px;">-</td>
                        <td style="text-align: left;max-width:300px;">%s</td>
                        <td style="text-align: left;max-width:300px;">%s</td>
                    </tr>
                

            """ %(str(self.test_end_time), str(self.suite_name), str(name), str(self.statsBefore), str(self.statsAfter))

            live_logs_file.write(message)
            live_logs_file.close()

    def close(self):

        live_logs_file = open('KeywordsMemoryStatsListener.html','a+')
        message = """
            <table align="center">
                <tr>
                    <th>
                        <h4>Execution completed! </h4>
                    </th>
                </tr>
            </table>
        """

        live_logs_file.write(message)
        live_logs_file.close()

def get_cpu_and_memory_usage_stats():

    # gives a single float value
    cpu = psutil.cpu_percent(interval=1, percpu=False)

    # gives an object with many fields
    ram = psutil.virtual_memory()
    # you can convert that object to a dictionary 
    dictperf = dict(psutil.virtual_memory()._asdict())

    stats = "CPU Usage: " + str(cpu) + "\n" + "Memory Usage: " + str(dictperf)

    return stats

def get_current_date_time(format,trim):
    t = datetime.datetime.now()
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        t = t + datetime.timedelta(milliseconds=1)  # manually round up
    if trim:
        return t.strftime(format)[:-3]
    else:
        return t.strftime(format)