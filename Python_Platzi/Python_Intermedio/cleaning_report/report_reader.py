import yaml
import requests

def main():

    url = 'https://command.avidbots.com/api/v0/Data/8750519'
    r = requests.get(url, allow_redirects=True)
    open('8750519.yaml', 'wb').write(r.content)
    

    with open("report_1374727.yaml", "r") as yaml_file:
        try:
            parsed_file = yaml.safe_load(yaml_file)
            sectors = parsed_file.get("sectors")
            total_cleanable_area=0
            true_covered_area=0
            sectors_count = 0
            
            for i in range(len(sectors)):                
                # Total cleanable area = sumatory of per sector cleanable areas
                total_cleanable_area = total_cleanable_area+sectors[i]["cleanable_area"]
                true_covered_area = true_covered_area+sectors[i]["area"]
                sectors_count += 1
            
            coverage_percentage = true_covered_area / total_cleanable_area * 100

            print("True Covered Area = " + str(round(true_covered_area,2))+" ft^2")
            print("Total Cleanable Area = " + str(round(total_cleanable_area,2))+" ft^2")
            print("Coverage Percentage = " + str(round(coverage_percentage,2))+"%")
            print("Sectors count = " + str(sectors_count)+" sectors")


        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    main()