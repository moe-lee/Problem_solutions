class BigNumber() :
    def __init__(self, data) :
        self.number = []
        while data :
            self.number.append(data % 10000)
            data //= 10000
    
    def __len__(self) :
        return len(self.number)
    
    def add(self, operand) :
        carry = 0
        for i in range(0, len(self.number)) :
            self.number[i] += carry
            if i < len(operand) :
                self.number[i] += operand.number[i]
            carry = self.number[i] // 10000
            self.number[i] %= 10000
        
        if len(operand) > len(self.number) :
            for j in range(len(self.number), len(operand.number)) :
                self.number.append(operand.number[j])
                self.number[j] += carry
                carry = self.number[j] // 10000
                self.number[j] %= 10000
        if carry :
            self.number.append(carry)
    
    def double(self) :
        for i in range(len(self.number)) :
            self.number[i] *= 2
        carry = self.number[0] // 10000
        self.number[0] %= 10000
        i = 1
        while i < len(self.number) and carry != 0:
            self.number[i] += carry
            carry = self.number[i] // 10000
            self.number[i] %= 10000
        if carry :
            self.number.append(carry)
    
    def multiply(self, operand) :
        res = []
        for i in range(len(operand)) :
            for j in range(len(self.number)) :
                mid_tmp = self.number[j] * operand.number[i]
                if len(res) <= (i + j) :
                    res.append(mid_tmp)
                else :
                    res[i + j] += mid_tmp
        carry = self.number[0] // 10000
        self.number[0] %= 10000
        i = 1
        while i < len(self.number) and carry != 0:
            self.number[i] += carry
            carry = self.number[i] // 10000
            self.number[i] %= 10000
        if carry :
            res.append(carry)
        self.number = res
