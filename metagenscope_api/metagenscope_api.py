#! /usr/bin/env python

import requests
import json


class Uploader:

    def __init__(self, targetURL, username=None, password=None):
        self.targetURL = targetURL

    def _handleResponse(self, response):
        status = response.status_code
        if status >= 200 and status < 300:
            return True, response
        return False, response

    def _scrubName(self, name):
        return '_'.join(name.split('|'))
        
    def new_project(self, name, metadata={}, overwrite=False):
        url = '{}/api/projects/{}'.format(self.targetURL, name)
        data = {'metadata':{'key':'val'}}
        if overwrite:
            response = requests.put( url, json=data)
        else:
            raise NotImplementedError()
        return self._handleResponse(response)

    def new_experiment(self, name, dataType, metadata={}, overwrite=False):
        url = '{}/api/experiments/{}'.format(self.targetURL, name)
        data = {
            'data_type': dataType,
            'metadata':metadata
        }
        if overwrite:
            response = requests.put( url, json=data)
        else:
            raise NotImplementedError()
        return self._handleResponse(response)

    
    def new_sample(self, name, projectName, sampleType, metadata={}, overwrite=False):
        url = '{}/api/samples/{}'.format(self.targetURL, name)
        data = {
            'project_name': projectName,
            'sample_type' : sampleType,
            'metadata':metadata
        }
        if overwrite:
            response = requests.put( url, json=data)
        else:
            raise NotImplementedError()
        return self._handleResponse(response)

    def new_data_record(self, name, sampleName, expName, dataType, metadata={}, overwrite=False):
        name = self._scrubName(name)
        url = '{}/api/data/{}'.format(self.targetURL, name)
        data = {
            'sample_name': sampleName,
            'experiment_name': expName,
            'data_type' : dataType,
            'metadata':metadata
        }
        if overwrite:
            response = requests.put( url, data=data)
        else:
            raise NotImplementedError()
        return self._handleResponse(response)

    def new_result(self, name, dataRecName, moduleName, filenames=[], overwrite=False):
        name = self._scrubName(name)
        dataRecName = self._scrubName(dataRecName)
        url = '{}/api/data/{}/results/{}'.format(self.targetURL, dataRecName, moduleName)
        files = {fname: open(fname, 'rb') for fname in filenames}
        if overwrite:
            response = requests.put( url, files=files)
        else:
            raise NotImplementedError()
        return self._handleResponse(response)

    
    
    
'''    

@main.command()
def get_projects():
    url = '{}/api/projects'.format(TARGET_URL)
    response = requests.get( url)
    response = response.json()
    pretty_print(response)

################################################################################
# SAMPLES
################################################################################

@main.command()
@click.option('--name', prompt='SAMPLE NAME', help="Name for the sample")
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--latitude', prompt='LATITUDE', help="Latitude where the sample was taken")
@click.option('--longitude', prompt='LONGITUDE', help="Longitude where the sample was taken")
@click.option('--surface', prompt='SURFACE', help="Surface that the sample was taken from")
@click.option('--date', prompt='DATE', help="Date the sample was taken")
def new_env_sample(name, project, latitude, longitude, surface, date):
    url = '{}/api/projects/{}/samples/enviromental'.format(TARGET_URL,project)
    data = {
        'name':name,
        'latitude':latitude,
        'longitude':longitude,
        'surface':surface,
        'date':date
    }
    response = requests.post( url, data=data)
    response = response.json()
    pretty_print(response)

@main.command()
@click.option('--name', prompt='SAMPLE NAME', help="Name for the sample")
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--latitude', prompt='LATITUDE', help="Latitude where the sample was taken")
@click.option('--longitude', prompt='LONGITUDE', help="Longitude where the sample was taken")
@click.option('--surface', prompt='SURFACE', help="Surface that the sample was taken from")
@click.option('--date', prompt='DATE', help="Date the sample was taken")
@click.option('--pet', prompt='PET', help="Type of pet")
@click.option('--job', prompt='JOB', help="Profession")
@click.option('--sex', prompt='SEX', help="Gender")
@click.option('--ancestry', prompt='ANCESTRY', help="Ancestry")
@click.option('--carry-phone', prompt='CARRY PHONE', help="Carry phone in...")
@click.option('--antibiotics', prompt='ANTIBIOTICS', help="Recently taken antibiotics")
def new_env_sample(name, 
                   project, 
                   latitude, 
                   longitude, 
                   surface, 
                   date, 
                   pet, 
                   job, 
                   sex, 
                   ancestry, 
                   carryPhone, 
                   antibiotics):
    url = '{}/api/projects/{}/samples/enviromental'.format(TARGET_URL,project)
    data = {
        'name':name,
        'latitude':latitude,
        'longitude':longitude,
        'surface':surface,
        'date':date,
        'pet':pet,
        'job':job,
        'sex':sex,
        'ancestry':ancestry,
        'carry_phone':carryPhone,
        'antibiotics':antibiotics
    }
    response = requests.post( url, data=data)
    response = response.json()
    pretty_print(response)

@main.command()
@click.option('--filename', prompt='FILENAME', help="Name for the sample")
@click.option('--name-col', prompt='SAMPLE NAME', help="Name for the sample")
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--latitude', prompt='LATITUDE', help="Latitude where the sample was taken")
@click.option('--longitude', prompt='LONGITUDE', help="Longitude where the sample was taken")
@click.option('--date', prompt='DATE', help="Date the sample was taken")
@click.option('--pet-col', prompt='PET', help="Type of pet")
@click.option('--job-col', prompt='JOB', help="Profession")
@click.option('--sex-col', prompt='SEX', help="Gender")
@click.option('--ancestry-col', prompt='ANCESTRY', help="Ancestry")
@click.option('--carry-phone-col', prompt='CARRY PHONE', help="Carry phone in...")
@click.option('--antibiotics-col', prompt='ANTIBIOTICS', help="Recently taken antibiotics")
def upload_many_phone_samples(filename,
                              project,
                              latitude,
                              longitude,
                              date,
                              nameCol,
                              petCol,
                              jobCol,
                              sexCol,
                              ancestryCol,
                              carryPhoneCol,
                              antibioCol,
                              sep='\t',
                              excel=False):
    df = pd.read_csv(filename, sep=sep, header=0)
    for row in df.iterrows():
        new_env_sample(row[nameCol],
                       project,
                       latitude,
                       longitude,
                       'glass',
                       date,
                       row[petCol],
                       row[jobCol],
                       row[sexCol],
                       row[ancestryCol],
                       row[carryPhoneCol],
                       row[antibioCol].lower() in ['y', 'yes', '1', 'true', 't'])
    
    

@main.command()
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
def get_samples(project):
    url = '{}/api/projects/{}/samples'.format(TARGET_URL, project)
    response = requests.get( url)
    response = response.json()
    pretty_print(response)

@main.command()
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--sample', prompt='SAMPLE NAME', help="Name for the sample")
def get_sample(project, sample):
    url = '{}/api/projects/{}/samples/{}'.format(TARGET_URL, project, sample)
    response = requests.get( url)
    response = response.json()
    pretty_print(response)

################################################################################
# TOOLS
################################################################################

@main.command()
@click.option('--name', prompt='NAME', help="Tool name")
@click.option('--ref', prompt='REF', help="Reference db")
@click.option('--version', prompt='VERSION', help="version")
@click.option('--desc', prompt='DESC', help="description")
def new_tool(name, ref, version, desc):
    url = '{}/api/tools'.format(TARGET_URL)
    data = {'name': name,
            'reference': ref,
            'version': version,
            'description': desc
    }
    response = requests.post( url, data=data)
    response = response.json()
    pretty_print(response)
    
@main.command()
def get_tools():
    url = '{}/api/tools'.format(TARGET_URL)
    response = requests.get( url)
    response = response.json()
    pretty_print(response)

################################################################################
# RESULTS
################################################################################

@main.command()
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--sample', prompt='SAMPLE NAME', help="Name for the sample")
@click.option('--tool', prompt='TOOL NAME', help="Name for the tool")
@click.option('--file', prompt='FILE', help="File to upload")
def new_result(project, sample, tool, file):
    url = '{}/api/projects/{}/samples/{}/tools/{}'.format(TARGET_URL,project,sample,tool)
    files = {'file': open(file, 'rb')}
    response = requests.post( url, files=files)
    response = response.json()
    pretty_print(response)

@main.command()
@click.option('--project', prompt='PROJECT NAME', help="Name for the project")
@click.option('--sample', prompt='SAMPLE NAME', help="Name for the sample")
@click.option('--tool', prompt='TOOL NAME', help="Name for the tool")
def get_result(project, sample, tool):
    url = '{}/api/projects/{}/samples/{}/tools/{}'.format(TARGET_URL, project, sample, tool)
    response = requests.get( url)
    response = response.json()
    pretty_print(response)







if __name__ == '__main__':
    main()
'''
