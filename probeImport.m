function table = probeImport(probeFileName,startId,idResolution)

s = load(probeFileName);

table = [];

for ii=1:size(s,1)
    row = round((s(ii,1)-startId)/idResolution + 1);
    col = round((s(ii,2)-startId)/idResolution + 1);
    val = s(ii,3);
    table(row,col) = val;
end
    
return