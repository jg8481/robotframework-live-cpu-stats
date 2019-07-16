import os 
import webbrowser
import psutil

class MemoryStatsListener:

    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):

        live_logs_file = open('MemoryStats.html','w')

        message = """
        <html>
            <head>
                <title>Live Memory Stats</title>
                <meta http-equiv="refresh" content="5" >
                <style>
                    table {  
                        color: #333; /* Lighten up font color */
                        font-family: Consolas, Helvetica, Arial, sans-serif;
                        table-layout: fixed;
                        width: 100%;
                        font-size: 14px;
                    }

                    td, th { border: 1px solid #CCC; height: 30px; } /* Make cells a bit taller */

                    th {  
                        background: #F3F3F3; /* Light grey background */
                        font-weight: bold; /* Make sure they're bold */
                    }

                    td {  
                        background: #FAFAFA; /* Lighter grey background */
                        text-align: center; /* Center our text */
                        width: 100; 
                        /* css-3 */
                        white-space: -o-pre-wrap; 
                        word-wrap: break-word;
                        white-space: pre-wrap; 
                        white-space: -moz-pre-wrap; 
                        white-space: -pre-wrap;
                    }
                </style>
            </head>
            <body>
            <table>
                <tr>
                    <th> >>>>> Generating Live Stats - Scroll Down for latest <<<<< </th>
                </tr>
            </table>
                </br>
        
        """

        live_logs_file.write(message)
        live_logs_file.close()

        current_dir = os.getcwd()
        filename =  current_dir + '/MemoryStats.html'

        webbrowser.open_new_tab(filename)

    def start_suite(self, data, result):
        self.test_count = len(data.tests)

        if self.test_count != 0:

            live_logs_file = open('MemoryStats.html','a+')

            message = """
                <table>
                    <tr>
                        <th style="background-color:LIGHTSTEELBLUE">Suite (Tests)</th>
                        <th style="background-color:LIGHTSTEELBLUE">Test Name</th>
                        <th style="background-color:LIGHTSTEELBLUE">Stats Before</th>
                        <th style="background-color:LIGHTSTEELBLUE">Stats After</th>
                    </tr>
                    <tr>
                        <td style="background-color:LAVENDER">%s ( %s )</td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </table>

            """ %(str(data.name),str(len(data.tests)))

            live_logs_file.write(message)
            live_logs_file.close()
    
    def start_test(self, data, test):
        if self.test_count != 0:
            live_logs_file = open('MemoryStats.html','a+')
            self.statsBefore = get_cpu_and_memory_usage_stats()

            message = """
                <table>
                    <tr>
                        <td></td>
                        <td style="background-color:LIGHTBLUE">%s</td>
                        <td></td>
                        <td></td>                        
                    </tr>
                </table>

            """ %(str(test))

            live_logs_file.write(message)
            live_logs_file.close()
    
    def end_test(self, data, test):
        if self.test_count != 0:
            live_logs_file = open('MemoryStats.html','a+')
            self.statsAfter = get_cpu_and_memory_usage_stats()

            message = """
                <table>
                    <tr>
                        <td></td>
                        <td></td>
                        <td style="text-align: left;">%s</td>
                        <td style="text-align: left;">%s</td>
                    </tr>
                </table>

            """ %(str(self.statsBefore), str(self.statsAfter))

            live_logs_file.write(message)
            live_logs_file.close()

    def close(self):

        live_logs_file = open('MemoryStats.html','a+')
        message = """
            <table>
                <tr>
                    <th>Execution completed! </th>
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