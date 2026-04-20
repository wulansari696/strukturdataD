import streamlit as st
import time

# NODE
class Node:
    def __init__(self, data, durasi):
        self.data = data
        self.durasi = durasi
        self.next = None


# CIRCULAR LINKED LIST
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, durasi):
        new_node = Node(data, durasi)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head



# STATE
if "jalan" not in st.session_state:
    st.session_state.jalan = False



# VISUAL LAMPU
def tampilkan(warna, sisa):
    if warna == "MERAH":
        st.markdown(f"<h1 style='color:red;'>🔴 MERAH ({sisa})</h1>", unsafe_allow_html=True)
    elif warna == "HIJAU":
        st.markdown(f"<h1 style='color:green;'>🟢 HIJAU ({sisa})</h1>", unsafe_allow_html=True)
    elif warna == "KUNING":
        st.markdown(f"<h1 style='color:orange;'>🟡 KUNING ({sisa})</h1>", unsafe_allow_html=True)


# PROGRAM
st.title("🚦 Simulasi Lampu Lalu Lintas")

lampu = CircularLinkedList()
lampu.insert("MERAH", 40)
lampu.insert("HIJAU", 20)
lampu.insert("KUNING", 5)

col1, col2 = st.columns(2)

with col1:
    if st.button("START"):
        st.session_state.jalan = True

with col2:
    if st.button("STOP"):
        st.session_state.jalan = False


placeholder = st.empty()

# LOOP
if st.session_state.jalan:
    current = lampu.head

    while st.session_state.jalan:
        for i in range(current.durasi, 0, -1):
            if not st.session_state.jalan:
                break

            with placeholder.container():
                tampilkan(current.data, i)

            time.sleep(1)

        current = current.next