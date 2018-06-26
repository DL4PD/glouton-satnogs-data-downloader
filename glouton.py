#!/usr/bin/python

from datetime import datetime
from services.observation.observationsService import ObservationsService
from domain.parameters.programCmd import ProgramCmd
import argparse
import sys


def glouton():
    print("""                   .-'''-.                     .-'''-.                """)
    print("""          .---.   '   _    \                  '   _    \              """)
    print("""          |   | /   /` '.   \               /   /` '.   \    _..._    """)
    print("""  .--./)  |   |.   |     \  '              .   |     \  '  .'     '.  """)
    print(""" /.''\\   |   ||   '      |  '          .| |   '      |  '.   .-.   . """)
    print("""| |  | |  |   |\    \     / /         .' |_\    \     / / |  '   '  | """)
    print(""" \`-' /   |   | `.   ` ..' /_    _  .'     |`.   ` ..' /  |  |   |  | """)
    print(""" /("'`    |   |    '-...-'`| '  / |'--.  .-'   '-...-'`   |  |   |  | """)
    print(""" \ '---.  |   |           .' | .' |   |  |                |  |   |  | """)
    print("""  /'""'.\ |   |           /  | /  |   |  |                |  |   |  | """)
    print(""" ||     ||'---'          |   `'.  |   |  '.'              |  |   |  | """)
    print(""" \'. __//                '   .'|  '/  |   /               |  |   |  | """)
    print("""  `'---'                  `-'  `--'   `'-'                '--'   '--' """)
    print('\tSATNOGS DATA DOWNLOADER')
    print('\t-----------------------\n')


if __name__ == "__main__":
    try:
        glouton()
        parser = argparse.ArgumentParser(description='Execute get request.')
        parser.add_argument('--norad', '-n', dest='norad_id', required=True,
                            help='the norad satellite id')
        parser.add_argument('--gsid', '-g', dest='ground_station_id',
                            help='the ground station id')
        parser.add_argument('--sdate', '-s', dest='start_date', required=True,
                            help='start date (ex: 2018-01-20T00:51:54)')
        parser.add_argument('--edate', '-e', dest='end_date', required=True,
                            help='end date (ex: 2018-01-21T00:51:54)')
        parser.add_argument('--wdir', '-w', dest='working_dir', default='.',
                            help='the working directory')
        parser.add_argument('--auto', '-a', dest='auto',
                            help='download new sat data automatically (not implemented yet!)')
        parser.add_argument('--payload', '-p', dest='download_payload', default=False, action="store_true",
                            help='download payload data')
        parser.add_argument('--waterfall', '-f', dest='download_waterfall', default=False, action="store_true",
                            help='download waterfall data')
        parser.add_argument('--demoddata', '-d', dest='download_demoddata', default=False, action="store_true",
                            help='download demod data')
        parser.add_argument('--demodm', dest='demoddata_modules', default=None,
                            help='list of the modules to use while downloading demoddata separated by a ,')
        parser.add_argument('--payloadm', dest='payload_modules', default=None,
                            help='list of the modules to use while downloading demoddata separated by a ,')
        parser.add_argument('--waterfallm', dest='waterfall_modules', default=None,
                            help='list of the modules to use while downloading waterfall separated by a ,')
        args = parser.parse_args()
        start_date = datetime.strptime(args.start_date, '%Y-%m-%dT%H:%M:%S')
        end_date = datetime.strptime(args.end_date, '%Y-%m-%dT%H:%M:%S')
        payload_modules = None
        demoddata_modules = None
        waterfall_modules = None
        if args.payload_modules is not None:
            payload_modules = args.payload_modules.split(',')
        if args.demoddata_modules is not None:
            demoddata_modules = args.demoddata_modules.split(',')
        if args.waterfall_modules is not None:
            waterfall_modules = args.waterfall_modules.split(',')
        cmd = ProgramCmd(args.norad_id,
        args.ground_station_id,
        start_date,
        end_date, args.working_dir,
        args.download_payload,
        args.download_waterfall,
        args.download_demoddata,
        payload_modules,
        demoddata_modules,
        waterfall_modules)

        obs = ObservationsService(cmd)
        obs.extract()
        print("\n\nall jobs are finished\t(   ^ o^)\m/")
    except KeyboardInterrupt:
        print("Exit...")
        sys.exit()
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(ex)

# -s 2017-05-20T00:51:54 -e 2017-09-20T00:51:54 -n 25338
# -s 2018-01-20T00:51:54 -e 2018-01-21T00:51:54 -n 28654
# -s 2017-05-20T00:51:54 -e 2017-09-20T00:51:54 -n 25338 --waterfallmf TestModule
