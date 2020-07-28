action_str = input("请输入希望执行的操作")
print("您选择的操作是 【%s】" % action_str)
if action_str in ["1", "2", "3"]:
    pass
elif action_str == "0":
    pass
else:
    print("您输入的不正确，请重新选择")
