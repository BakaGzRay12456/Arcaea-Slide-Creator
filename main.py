import algorithm

if __name__ == "__main__":
    res=''

    x_start=float(input("Hold开始x坐标："))
    x_end=float(input("Hold结束x坐标："))

    while True:
        timing_start=int(input("\nHold开始时间："))
        timing_end=int(input("Hold结束时间："))
        if timing_start<timing_end:break
        print("Hold的结束时间需大于开始时间！\n")

    algorithm.show_ease_menu()
    ease_func = algorithm.get_ease_choice()

    values = algorithm.interpolate_list(x_start, x_end, timing_end-timing_start, ease_func)
    
    for x in range(len(values)):
        t1, t2, lane = timing_start+x,timing_start+x+1,algorithm.ArcAlgorithm.laneToFloat(float(values[x]))
        res += f"hold({t1},{t2},{lane});\n"
    with open('res.txt', 'w', encoding='utf-8') as file:
        file.write(res)
        file.close()
        print("\n已生成于res.txt！")