from    dotenv import load_dotenv
import  json
import  os
import  requests

def get_study_data():
    response = requests.get(API_SERVER)
    print(f"Response: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.text)
        return None

def main():
    data = get_study_data()
    outpath = os.path.join(os.path.relpath('data'), 'clinicaltrials_api_response.json')
    with open(outpath, 'w') as outfile:
        json.dump(data, outfile)

if __name__=="__main__":
    load_dotenv()
    API_SERVER = os.getenv('API_SERVER')
    print(f"Pulling data from {API_SERVER = }")
    main()
    print("Done")