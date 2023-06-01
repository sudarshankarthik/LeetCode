class Solution:
    def trap(self, height: List[int]) -> int:
        stPtr = 0
        ctPtr = stPtr + 1
        vol = 0

        while stPtr < len(height) - 1:
            tmpVol = 0
            while height[ctPtr] < height[stPtr] and ctPtr < len(height) - 1:
                tmpVol += height[stPtr] - height[ctPtr]
                ctPtr += 1
                if ctPtr == len(height) - 1 and height[ctPtr] < height[stPtr]:
                    print('edge detected',stPtr,ctPtr)
                    tmpVol = 0
                    ctPtr = stPtr + 1
                    break
            stPtr = ctPtr
            ctPtr = stPtr + 1
            vol += tmpVol
            print(vol)
        
        return vol