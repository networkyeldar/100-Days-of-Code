import pandas

data = pandas.read_csv("data.csv")
gray_squirels_count = (sum(data["Primary Fur Color"] == "Gray"))
red_squirels_count = (sum(data["Primary Fur Color"] == "Cinnamon"))
black_squirels_count = (sum(data["Primary Fur Color"] == "Black"))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirels_count,red_squirels_count,black_squirels_count]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
