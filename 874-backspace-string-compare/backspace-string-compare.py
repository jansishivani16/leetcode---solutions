class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            st=[]
            for ch in string:
                if ch=='#' and st:
                    st.pop()
                else:
                    if ch!='#':
                        st.append(ch)
            return "".join(st)
        return helper(s)==helper(t)
