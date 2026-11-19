class stack:
    def __init__(self,data):
        self.data = data
    def add_to_stack(self,*new):
        for v in new:
            self.data.append(v)
        print(self.data)
    def rmv_frm_stack(self):
        self.data.pop()
        print(self.data)

st = stack([1,2,3,4,5])
st.rmv_frm_stack()
st.add_to_stack(1)