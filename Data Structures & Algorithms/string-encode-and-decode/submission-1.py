class Solution:

    # Function that converts a string  
    def encode(self, strs: List[str]) -> str:
        packet_to_send = ""
        # Loop through list
        for word in strs:
            # For each string, get the length, and append '#' with the length with the string itself
            packet_to_send += "#" + str(len(word)) + "." + word
        
        return packet_to_send

    # #5.hello#5.world
    def decode(self, s: str) -> List[str]:
        result = []
        # Loop through the string s
        i = 0
        while i < len(s):
            word = ""
            # If we encounter a '#'
            if s[i] == "#":
                # Get everything up to the . and convert to number
                i += 1
                num = ""
                while s[i] != '.':
                    num += s[i]
                    i += 1

                num_int = int(num)

                i += 1

                max_ch = i + num_int 

                while i < max_ch:
                    word += s[i]
                    i+=1

                result.append(word)
       

        return result




