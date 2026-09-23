class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        

        #power of 2^n - 2^n - 1 is covered by / (32 - n)
        #so x/
        def num_to_bit(lst):
            x = 0

            for part in lst.split("."):
                x = x * 256 + int(part)
            return x
        
        def bit_to_int(num):
            return ".".join([str((num >> 24) & 255),str((num >> 16) & 255), str((num >> 8) & 255), str(num & 255)])

        ip_list = ip.split(".")
        curr = num_to_bit(ip)
        ans = []
        
        while n > 0:
            block_size = curr & -curr

            if block_size == 0:
                block_size = (1 << 32)
            
            while block_size > n:
                block_size //=2
            free_bits = block_size.bit_length() - 1
            prefix = 32 - free_bits

            ans.append(bit_to_int(curr) + "/" + str(prefix))
            curr += block_size
            n -= block_size
        
        return ans

