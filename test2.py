

# # ��������flow�ı���
# flow_control = []
#
#
# def get_flow(flow_name):
#     for f in flow_control:
#         if f.name == flow_name:
#             return f
#     io.warn('û����Ϊ' + flow_name + '��flow��������ע���flow���£�')
#     for f in flow_control:
#         io.printl(f.name)
#     io.warn('��ʾ���')
#     return None
#
#
# def reg_flow(the_flow):
#     if not the_flow.name in [x.name for x in flow_control]:
#         flow_control.append(the_flow)
#         return
#     io.warn(the_flow.name + '���ܱ�ע�ᣬ��Ϊ����ͬ��flow����')
#
#
# def del_flow(flow_name):
#     f = get_flow(flow_name)
#     if f == None:
#         io.warn(flow_name + 'û���ҵ����޷�ɾ��')
#
#     flow_control.remove(f)
#
#
# # ��ִ��flow�ķ���
#
#
# class Flow:
#     def __str__(self):
#         return self.name
#
#     def __init__(self, name):
#         self.name = name  # flow_name
#         reg_flow(self)
#         # self.next_flow = None  # flow_name
#         self.cmd_dic = {}
#         self.runable = True
#         self.sendmsg = None
#         self.innerflow_map = {}
#
#         # Ԥ��innerflow����
#         # ����ַ���
#         def getstr():
#             self.sendmsg = io.getorder()
#
#         self.create_innerflow('getstr', getstr)
#
#         # �������
#         def getint():
#             number = io.getorder()
#             if number.isdigit():
#                 self.sendmsg = int(io.getorder())
#                 self.run_generator()  # ��Ҫ�����Լ��趨������������������ѭ����һ�γ���
#             else:
#                 io.printl('���벻����Ч����')
#
#         self.create_innerflow('getint', getint)
#
#         # �ȴ�һ���س�����
#         def waitenter():
#             return
#
#         self.create_innerflow('waitenter', waitenter)
#
#         return
#
#     # ��������ʾ������
#     def func(self):
#         pass
#
#     def run(self):
#         self.cmd_dic = {}
#         self.bind()
#         self.func_generator = self.func()
#         if str(self.func_generator.__class__) == "<class 'generator'>":
#             self.run_generator()
#
#     def run_generator(self):
#         self.bind()
#         try:
#             request = self.func_generator.send(self.sendmsg)
#             called_func = self.innerflow_map[request]
#             io.bind_return(called_func)
#
#         except StopIteration:
#             pass
#
#     def create_innerflow(self, name, func, auto_reture=True):
#         def innerflow(*args):
#             func()
#             if auto_reture == True:
#                 self.run_generator()
#
#         self.innerflow_map[name] = innerflow
#
#     # �������ķ���
#     def cmd(self, order_number, cmd_str, flow_name):
#         if order_number in self.cmd_dic.keys():
#             io.warn('�����ͻ��' + str(order_number) + '�ѱ�ʹ��' + cmd_str)
#         self.cmd_dic[order_number] = flow_name
#         return cmd_str
#
#     def bind(self):
#         io.bind_return(self.goto_flow)
#
#     def goto_flow(self, *args):
#         order = io.getorder()
#         if order == '':
#             io.clearorder()
#             self.enter_default()
#         if order.isdigit() and (int(order) in self.cmd_dic.keys()):
#             io.clearorder()
#             next_flow = get_flow(self.cmd_dic[int(order)])
#             next_flow.run()
#
#     # �����»س�ʱ��û������ʱ����ִ�еĺ���
#     def enter_default(self):
#         pass