#! /usr/bin/env python

import requests
import click

class API:
    def __init__(self, url):
        self.url = url 

    def new_project(self,name):
        url = '{}/api/projects'.format(self.url)
        data = {'name':name}
        response = requests.post( url, data=data)
        response = response.json()
        return response

    def get_projects(self):
        url = '{}/api/projects'.format(self.url)
        response = requests.get( url)
        response = response.json()
        return response

    def new_env_sample(self, name, project, latitude, longitude, surface, date):
        url = '{}/api/projects/{}/samples/enviromental'.format(self.url,project)
        data = {
            'name':name,
            'latitude':latitude,
            'longitude':longitude,
            'surface':surface,
            'date':date
        }
        response = requests.post( url, data=data)
        response = response.json()
        return response

    def new_phone_sample(self,
                       name, 
                       project, 
                       latitude, 
                       longitude, 
                       surface, 
                       date,
                         city,
                         food,
                       pet, 
                       job, 
                       sex, 
                       ancestry, 
                       carryPhone, 
                       antibiotics):
        url = '{}/api/projects/{}/samples/phone'.format(self.url,project)
        data = {
            'name':name,
            'latitude':latitude,
            'longitude':longitude,
            'surface':surface,
            'date':date,
            'city':city,
            'food':food,
            'pet':pet,
            'job':job,
            'sex':sex,
            'ancestry':ancestry,
            'carry_phone':carryPhone,
            'antibiotics':antibiotics
        }
        response = requests.post( url, data=data)
        response = response.json()
        return response

    def get_samples(self, project):
        url = '{}/api/projects/{}/samples'.format(self.url, project)
        response = requests.get( url)
        response = response.json()
        return response

    def get_sample(self, project, sample):
        url = '{}/api/projects/{}/samples/{}'.format(self.url, project, sample)
        response = requests.get( url)
        response = response.json()
        return response

    def new_tool(self, name, ref, version, desc):
        url = '{}/api/tools'.format(self.url)
        data = {'name': name,
                'reference': ref,
                'version': version,
                'description': desc
        }
        response = requests.post( url, data=data)
        response = response.json()
        return response
    
    def get_tools(self):
        url = '{}/api/tools'.format(self.url)
        response = requests.get( url)
        response = response.json()
        return response


    def new_result(self, project, sample, tool, filename):
        url = '{}/api/projects/{}/samples/{}/tools/{}'.format(self.url,project,sample,tool)
        files = {'file': open(filename, 'rb')}
        response = requests.post( url, files=files)
        response = response.json()
        return response

    def get_result(self, project, sample, tool):
        url = '{}/api/projects/{}/samples/{}/tools/{}'.format(TARGET_URL, project, sample, tool)
        response = requests.get( url)
        response = response.json()
        return response



