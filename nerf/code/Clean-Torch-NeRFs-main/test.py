from tensorboard.backend.event_processing import event_accumulator  # 导入tensorboard的事件解析器

ea = event_accumulator.EventAccumulator("logs/mine")  # 初始化EventAccumulator对象
ea.Reload()  # 这一步是必须的，将事件的内容都导进去
print(ea.scalars.Keys())  # 我们知道tensorboard可以保存Image scalars等对象，我们主要关注scalars
train_loss = ea.scalars.Items("train_loss")  # 读取train_loss

# from torch.utils.tensorboard import SummaryWriter
#
# writer = SummaryWriter("logs/mine")
# writer.add_scalars('asdf',{'a':1,'b':1},1)
# writer.add_scalars('asdf',{'a':2,'b':2},1)
# writer.close()