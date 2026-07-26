# import greeting as grt

# # print("app.py is running..")
# print("my name is:",__name__)

# grt.hello()


names = ["telegraf", "influxdb", "grafana"]
# upper = []
# for n in names:
#     upper.append(n.upper())

upper=[i.upper() for i in names]
print(upper)


files = ["model.engine", "config.txt", "yolo.engine", "readme.md"]
# engines = []
# for f in files:
#     if f.endswith(".engine"):
#         engines.append(f.replace(".engine", ""))

engines=[f.replace(".engine","") for f in files if f.endswith(".engine")]
print(engines)


gpus = [("Multi-cam03", "3060 Ti"), ("serv-i1-gpu1", "1080 Ti")]
# gpu_map = {}
# for machine, card in gpus:
#     gpu_map[machine] = card

