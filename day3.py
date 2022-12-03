import string
puzzleInput = """wgqJtbJMqZVTwWPZZT
LHcTGHQhzrTzBsZFPHFZWFFs
RnLRClzGzRGLGLGCNRjTMjJfgmffSffMqNgp
WPLgsfLmLgqZvZgSRR
RbwHdbDdQFFFMvvMjbhqhZZS
lzTdldBDszfGcRsr
ZjnhJjMjnbdnbHdFLmmfFLmnCCWFFl
PpNwtRsNsZSsRwCfzQQBfQszCBsC
PpwcqqVZRtbggggjcgJJ
ntczBcVcgnHzgBHnVntcBBFhgsmmmssqWNWNWqLvNhsqTN
bSSGdSDZbGSGdDmLmGTvTGmLFFhm
PlFbDpJDPbPdPbZQZDZlSCDBfMVRwBzBtBQzfzRHVMVRtH
fDVrmmrvcmCcVpfcfGlswpPwsttMpjJMPPjjtP
RgSTdndFLbJqqPssWWjPWjPjHS
FqgzQnTqJRRQqLLhTCDhDCDmcmlvvlhcVm
nnqVtHbfVHZVmtlvmHtZtrFSFTRRFhRccTbrLsLSGr
cCNJQJPJQgjjMQdDrGGsRhTFGFRFSpMS
gzdCwWdjNPgzcJgjwdZtVlHHmvvmZlvffHnz
FFgsgwNwWvggQsMWDwvQQvQcccdcJZDtJGBtVGGGtcVlzt
rjfTrbjpjRSRTbTpzldjjHBtJGBdltJG
RbrPTfpCfmbpmnfRRCvMvQWNBwFFgMsgBL
zzLHgjjjdFHWbGBjjzcbgQRmSvqsSpmRsRSQSmRMWv
ZfJVrwPhZhZlhQQqBSQSNSqM
tnCfrDCltfPzHFFLBgngHz
DCpwrrMhwCrCMVCpGFqpVDnWWTWBtnTWvWfvbbTdFWRv
lmhhcsQPmTtTnnPBTB
QmcjNJsJzHNljZsNqDCGGhwqCqhgDDZV
hLfRnSLfhcndCCPfJJjzJfzt
pHNWwDpGGNJBZjjNNj
gmgwwHpWTpmGDmDTggqHmmDSsnnhvcqScdVVSVcjLrRcnq
CdlTJgnQJVCllNVWTPZBmPPGhGRmghPRGs
wHDrSwtHbmhRvHVZ
DzzwrtVFjLNnMTCTLCWW
SppdsnGpNVnZZZLPMlMPGq
mdcfvTTbBddLJgZJLlcFqJ
fzTvfwjjfzzCbvvjvQjWvNHVNNVWrRtdnVNppNprDp
lmlCGTmNbZlbSFlbNGfnzWfWzCdWWfVdwRCf
jDHtHHvLjQtqrsqpjBBLprRzwfwJfzzhRnczhWQVwzVR
rqpPtpPjDqpqDLtLrPGGFSFgPlNZZSGMPnMZ
pSHShqgSMzVpphFnJMFMBtssdjRJ
PZDbZfmCDgDfDNQPwCflCQNJsjRBRBFsdBWBsJRjsbsFJF
DQvCwwZrPPlffDmQCDwZQPmPhqVTcGhSHSLTpSGhLHzpGghr
gPqgqqmmmPgsqvGmsMCCnfZZfvBpWZhVrrZdHBvH
TSlcttTjRTDlDDTRhZVdrHHpWVnfVrtd
SFJzFzcJjcRJwGGqJMMCwW
gzWNLSjRLzlNqqQMLhvQccGGmcQm
fFrttPdTFTrpVwGpbdVQQp
HnTBGfHTGzWWqCqngn
SddrLdVpjjVSgRBszFswzwlV
mtPMbMqPMvqHHHDTTglBvsFshFFg
bmBHbtPctMtbMNMtbPtPqHmMjpdZdcJGrjSWWZGjJZnjndWj
nljWJHRHGrDcMBbDLZHV
wdvwmhghhbtBMcLtwZ
gvQvvghTfPSmpmQljGFRjQbFGCsJbC
BmphBWmDBBQfpVgQZpjg
rqqGrrrqlnqqHqjNnVDSSSgQQffj
FqLrbsLFsbLbLqHlMrmwwPDcCmMMmJBwDJcC
wZccfslqZPFFjrFbFfQQ
vvTvVWCJJZVBWCSvnVJJrhjQVMjVjzbgMQbjpphh
BBmNWBvZRvSqwsGwssPcmc
LGpnfcnzfzQdNFNHqHJptq
RBNNvZSBRbRCCDJqHrDZqHFZtw
SRNhRsNhWSNWsRRvgjngQnnMTnTgQjGMff
twtZmwqBHtmqnnmlGLfcfvQQ
dgMSPSMdQGclRRdF
pVMrDgThDDlPWPWbBZtZqqttBqjqjT
PPSWCGSzpCCQwNsNPFhTNVbB
vqcgJngqLLcZLvBhNTVlbsvdFF
DDmHgRjHZhHtGfWpQH
sBLbwWWBvsBsqLqStRjcGGRnggjGcntJDn
NCMQPMQPMQNzGGRRgRJRGzcG
dHQNfPCFTQfFfVVNvwwJvSWSqWqrSqdS
prDBnnDpFDprnDPBDQBvpBZttcSqSZSZcScFJSHcZJtz
VhMVdLsjdqVWJSWZZZcHst
hLVdGLfqjGjlfhCfCLjTTmrlpQBPBmvnrgDgpp
SSSTJmmgbGwtmRZHCCZRCH
FWcPQrrWqflzSWpRHZCZHRSt
PSQzzdcQTghdndDJ
cLlrNPvljRhRgTlM
VmDBGnVdmJDnDBndnnVwDRvMgRsTbTzMMsgZghzzsB
SpHvmGnSDJnwvDQqfrCPLpPLCfpF
PppbRCCgpzzQCgCSgZTlNNTWnNNDNlRnGl
hwMhLtBcBdjjNzWzlclcNGTs
FjJFHJwhfwLHMLJLwPmqfQPgVCmQgCmCzC
jTtMqFjMBqBmTntTztBTnTZBRZRLpLJgDgJNhghJrNNhhLJh
DCDdvdGsVDVsflVdQSsfSwhRJlgppgpRpbWLgJbJpgbR
wfSHSsdSVvQSwfwQPQPqHtFDcMzmtjBntqMTqn
HQhQWLCSHCSCjnjQdSJdCSQgTTmZPTVZmqnTpPtnpmRmpp
vDrzhvGzfchvlGvMFMrqVqPgZVVtZtVRgZgm
bcvMfwvDsDfbvfwDbbdhCShWCBLLJWjHsHjj
zLSsJNCjsjLCNLCgGcwBPPdwBwqwqz
WMFZprZDbrddWRVRRDvlPPBcPhhlBqqHPGPhhffg
VdbFvZWWWZZDFTLtCmNntjTnLSnn
JLVhhwRbhVwcLFJFhhJcccqwsvpRlllvpWvZSBSSSRsNWpzl
jgzfPffgZNspgZQS
fjCmDCGnfmTfFqrFnhqbFzqt
SfMRRNHSNNLfRfHcRRsqwdCCsssTqBCvgBLv
llDDWQnFGtQnmtGQDWQFsgdHVBddndHsgqTsCTsg
GzGjpWmWbmQmbpGGmGjHSrZcMfZSRPJPfcMRcb
PDdMdRTRrLDSwzJvfSvJ
FnjQnsqsFTnStvplhhzzFS
TBHHCsgVRRcMHbLR
GcLdGBJvBvLJHccJBvqHpGzDFfzwfzjwhDwrSFpfpDSn
mZZrTTQVmQmlsMPVblZQVZmfCwjzzjChzCCbDSzhFjfnSb
gZlRlZNPlmlgTTPmNRvJWcqrNLdvHWLBcHtH
jWWbBwgwWwwtvvSCtHvgWsMFmscHzTGMmcssGFTTGz
ZrLtpLnlfQJqnfJtpLnZlrqdNNGqcDNNFFTNDzzMMTMsMNMs
LJQrnZnfLZnlrZflJJRVRQbbwBgCtCVjWgjBjjgbPjBB
fqQVfRqSqmpnlLnm
jFcjMJTjhwwggjFtgzCHmCzCmGzGlzpn
wstMFFjWDfQRvmDPSB
PgTFGPgcBZPcHPFBZRjGPgwCnmwCsmSdQdThmMMMQCQS
JbpvWtvfHblWDHJDzmndSdMQnSwCdhMdQD
rfvWlLlbtfJvvLJpqWbbqZRRGPVFNHVFgZNVFBgH
TRMrrGBLMLPtbssTGtBHwZmdQQbdNzzZZNZZdwjd
CVlVhCnclvhWSFFfQrWNrjmpNfwmjZ
rlqFlclChhCvnlDvgVvRRtPtqTGJHRMBRTPPqM
gZzCrQGQdrQvZHPTHWDbTgWPJM
nSpLlcnnVjsSVLLnLSnhLSsJPTTWFsqfbPMFMqJDbfqM
VwwnpwLnlPdQCwPPCC
lRlrnlrsrMlhVsRnVhGPvCFNcPBDBvccrCGr
RZQTzWTRdDNvBDdNcC
TqjZbWRHmlMJgnmsng
scQmLfQBQQvvZfLsmmvDJwpgSNSDDdcJSSwTGD
PHlMbtzCCnlbztMRzlPNNdNwGpDpwgwptNLGpw
rRHnLbhCzbbCHnHjMbzzjzFZmfQqWZQqvmhmfVZmqFBW
fLTQWTMQtjcCGCJCbf
gGsmsVSzmjCFHJCJgg
SPRsSwSvBsPRPsqzwSVqzmhVWtLWhTDNLlTDtLTWGpNMtDLt
mbzRbchRRQzzssLdhLggLddJ
DCqDNNNWvDvjcPLsJcLLdv
cpFCVNnVBHtbfFRtMRFf
PFRcCCPtsDDDtjVspgwmgTNpTgTpspsw
BqqqdJdHdMgSfMmZpZND
vDHJGdLbLzBJdGnDdrBqVtCzWPPhthtPFzzPCFtV
HvhvHdFdvJDfHdZdpfhrmGPljPRrGPPVDGrWWC
NMMsRBMzcRRMMBSzcnbmNGrCVCWrCqPClmPqlG
zLBbwMzQnRSQMThtZFLvpdgHtJfF
DpcJcJPmMcLSHHZCfpnH
BsBFvvqTFlbhgdbBBblfZLCLzfHWfjnjLCnCrh
dTsNgqFvNgsGlZJRtVtMPmtDmG
LdGQqzPGCCjJTJdTLJQJtFcFRSctcrFNFltPFtcc
HphMMbbMdBMHbBhhgHMnhvwFFvtrlSNRNgcRllcvcc
spHMhBnHnnsmWdnsnMBMdVGGmzjzLmZLDQCCCCZjqjTD
DDZMzcTRgDMLzqCffhfWfcWnfj
NsHVVJmswwSSwNPPNjnhqhnCCnhNvjfTnv
rSSddrGSGrlMrpTpQT
bbbfCfrLHMMMWVWC
SqsvNZqQvvqcjNvqZsMMwgFgFplTHQVRFgWH
BSZWWqBZBjmPGJGLbBtf
RNCNfzfRHmzHwSdRdGfzRJPqFcFcDFGccZZqtLtGLtgl
pjhVMhvhbjvPcDJvcZqt
bsQMTsjppmSdTnHSJH
PtLwpSwdSJwQnGvvqtvMhZ
TlFcHlTjVjsDTQnCQhbZGCVVnb
cjljTslTrlzzHDNRfNgLSNBJfBwNfG
HvsZZqqqwWZswWHTmHsvvfhSfBfDffjchfBbhD
MCpnCVpQClRNnlNQVQClfDhScmjBfLhmLDGbBNbS
gmtpJpQQllJnWdZWwJWFwJJT
TzBvBwwdhgRPGHlRHh
NLWttJsrLWttppLpsGlsmVbVGRljGDRgjV
MlllnNFnnQqCdzqq
vptzrJhMMGGMptJPhJGJPvdFTFcSsTBVsczBScTSFFfn
gbRjWgRjCqjZnfHCHnTSVBHF
mRwqNbmqlbbjqRNlLbNrDJntNDGtDhNpGMrpvJ
GPWZLgWqLHHGbgbbGPPmqHqfcjjRHJJBDRBRjBBjMHjwvwQc
dhpFSpzVSSMSlDBvMQ
TndsVNztVTspnsdpshtmZLPCGGNPfgqbWWfDGb
CbqDjjCdClqgrfJvrv
NGNPtGGzzHztPWWnlgJvfBnWBFgp
hGzNHhsmGccwHPHZHcwdCCdbTVRTvSmTCjbLCb
sqnqsHGpJbqnrbshpshHmmmCWZZmWwfTjTjHmfLZ
dPggRgSDDttMFgctgdDtDcDcRWJBmjTWwmRLBLfmwBBjZWTB
PFcVPlJPglbqhhrnnlNz
wZdDNDdPPfhqwWqbsF
VTngRzpnzMLvzTCLlhvDfltqqDttqFqs
mggTVpCDDSNjBmPZrd
cSdqJSTTTJcSJpCdQbqTCPPdjdDtGzwzjDwjwwwwzD
rVvsBBVgsVBhHhfljtgbPgGtWjPtwt
fvHsVZHVnRHpSJJRmbbSLT
lDDPRRjwLGlvVRDRPlwwwPvmpSfhVWSzhqfzqpHpVpVHfqSH
qBnqBNsBBChhCSfZ
nTQbQnNNQJTLvlmTPLqqmG
TTCJhDrmDpRVhvhHfffwzwfz
dmmdmglWcqvHvWsHzB
gdQMZbtlgQlZcMSttCNmVVrLSTTJ
PLZLqhZZzZLBjjjGrrPjMH
CcQcCcfRlWDjdrMrBrHC
WlWFMcFpcRFmsWFcmflqSJzTqzwLvshggsZJwz
LgqRDDDHHGTpgpJrQrQhhhCqrwPw
ZSBWjjFshCFlQDrJ
SjWnnbWtWnsztgGDDbDTGgHHGp
llfvMlvzjzGzGRfvMSGRfSdStrCtQNCZrrFdJJLnNtLZ
shhhshPHsTTqsBHTVTwTwZZnCtQrQnJtQCCJBCCZdZ
TPHTPTHmDnljplfpGfGm
qcNTmvvSvTNrWhRrTdthzW
bDVJphpMMJwJpMHtrrttWsgwtzRW
bFpGJbllPfplVQmnhvvcSmCFqq
GTPJGMQTPQMqZjHTBmnndBVddHrrzNrz
bbcRFgDpptRbffwmzmrvLmcZvmLmLv
WCwgWbpgwtgfpfMlQGPhSPZWTZPl
DsPCswsMPBMwPDCVJPnTPPWFGJNJmbJW
RvvddfvftdtvNzghGSbFnWTntJSttGbG
LNgRddgRlgzcgCDjjjHjcBCwcM
gnVtgBnpwBgShBgcwhJJhjCMMMDmLRjDRMjrDMMMDMqMRF
slsblHPNHlbTNbsPvszHQWbzqrZLMRmFMFmdFmrtDFdMLNZD
bPzfvbfsvvlHtlzPHllHGTlTppCJpgcngcpwnwCGGJnnShwV
cgQRgtzDbHPcgHzQWpTjTLdjjNNpNLsDss
nwccZBmwcJqmJnjsTvmlTSsdlTNs
CCGFCBVrBwwGBhqVnZBrqWMMQzHfQcHzzzPtfztGfg
lhnwnhlbgbngbcfDgJLJQqDdVd
FSrvtMFZVJJJVtcq
jZNNNNjmjSPjFTJmGGzswwzHwHpBsbPblhhW
tnDWHntzDtzQBZLMLzNLDDcRFFjhJBmcFRCTjRchcRvT
sqwsPlbGfSbPGSVbJfpjjhcTFmCRjjvmTTvRdw
lJqSqPVbgGSGrVSqJqflbWZQNDMLHnrQQWNDMtQMQz
lpltwwJqsWVLPtVt
DGHsDdZQzHLSLZcFRrFS
BGsGCnHmMlMwCfwT
nrRNzRMPrrPnNwNzTSFSTNtqZdtMttvQqQmjdjvZpgjZ
GWVhGcGhHhGcffbZGDmmtttQvpdtbpppdj
HGlHBhHGJfJJhCfZzLTTNnNrTnCNwT
jBpCZStjBwWrQCMrhw
TvcHBzHdPPzdvFTzzJlvzdQfThrhhrhfQTWMQfWMqfwf
bzGJJBJcJvdvBPFzddGgjZSbZZngRZNNnnsjRs
dqPqbpPFJfsFfMcNQNNtNmzrNQJn
VVBDWvwZWDLwGlDhLGWWVcmQtSNmLmtSdSSTmrcQQm
lZlhwDCdhhHllvWvjMHbgMpgffMggpPb
SWSFLLFWDSWDNFzmmLMfGlfsdfnJMBfwMGVnBf
vPtgZcctcTQQZRRcgCtZwRfqBVGqnVTBGVnqlsdBJnqV
RcjgwbbgNSbFbhDb
JrRZLrHvjQFPLnnBPQ
DhwbtHbzpcpFTgtQ
zlDwlHlzWSwDqhMMbSJVZVvrCrCZJZNZdJ
fgNCZSDtDfDZTrTfqWghQGzGQshgpGGFQg
RFvLnvFjnVjmLQGPQWLmWh
MdwwVMFbMdRHFbccbCZJtbDJrqqJZNJZCZ
fdZVBMMdfdfBCzhTzMdMCgCrGGrpQJmSmGJGmpJQVpLmqV
RbFnhNsvlDsFHttllGmqGpPLvJpmPJSqLL
tjNsDnNwbNjttNNZTzhMWzcZcMTwMd
DjSSMShjRjPCbDFCdCSDbpBBswfNWZBZZrBVBPNfVmVf
zltLjLqqGlzQntqqGztqcgncZrVrmNfNwWBVrVmrgwrfswsW
qcTqHLlnJzGznLJtHGhMbhjFhMMpFbpbThpp
ZVFZcctFQzsCtbZFnPPHqmqpwmvPmp
NrjGfMgcLLcfdLqpmRwRRqJJmdPw
LMNDgMBGlgGDLMNDGljctVbVWZTTCWChhTttsl
RMGRRhhgzgZMtHdGTtvDwDJFCDvvwdvwqFFv
rfrrjLNmmSnSjVSmNNPPbJVbqvqsqvhvFqCq
flrpnSlrSNfjrNjSphNSWlHRGzTgtQGHQtttBTRBRQHW
tplDDprhbvprvrJDprCpbsvHRfzSzTtzmRqSTznRRBRnSfFF
MVwWjVNVQGfcMnTmRnBm
VQwGLNLjWNWPGjZbsDBppBZhhDvBlZ
RVVrGVVchRZsnzRzBWZb
FQHWWCHwQmWmlqfCHSwJnsbNJnNsvttntBtb
QQSFgqgqLMLPPdWdMVhWDT
cZrMjncTdfJpPJbr
WHNqnQwwCwvlqHtCtHNslNlvLLPDfSVdVPVDVSfVSbftffVf
NCwwwQwllwnvgsvZzgzFZzBzjGGGMM
MvHpfzcTcZzpphhbsDSTStsltqSDtS
PRmnwCrWnWQrmNMRNnlNGbqlbDltdlbDtNtD
CRJnmRVWJfgMLvcz
HPFbHrrwLdVdgbDZqcphCqSZBhLZ
tQRfRRGtvTNNSGTMjjmDCRhmqpBChqhsRDZh
vjSfMzGQNQQnMtNTTWNNjgblFdFHwgdJJHHPwddgnr
BggPRVBPPgfCBmJTjTTqpTNpZBwMbr
lclLLllsQLFlsbMqNrMwTpwpcM
SvbDzSDbWFJfWPPgdnfR
GbpSSbGDNbSSJbDZNZbDppGtMntHLHvHCTLCJMHnRCMLTT
cdwddjBfPsmPPQqQqscnHgRMtngvtjjgCCTMzM
WvwPvWvflBwdQPlNVVhbDGpFhNGhbl
WZRGmRvpCRFTZMQQQMCdddDDcD
lqgqsgvjVtbMDzzbtcDQ
NsNNgjNNjsNhnSvRmnpGRmSTSG
nTgFtDTDDLrFBStdGdcHcbvGSc
QPzfPCMzWCjfMPJhWGlRbRWRWrRRdVVH
zhCrCQCjPrpNNBsNspNnwq
zTJpqFzbTzsWsVbbfLGfSSCDNSBCHfMLHG
rZcvtmhctrvmlPPmmmrhhmBLCHDCCLLDlqMlGMNDMwDC
rRhRhnnQPZhtZcZtdttZgqFWWVjssqQpppWpFpJW
NWPhdWJPWVzVqQrqmSsPbrPP
cZDRjGsffGsCDfffgjGgRQSrTcTmSlTrbnqmSSrlln
fFGCjGCjLDLFRgfDHZvzLVWtvsWWBtzJNWMB
qMVbtnmMMTpCppsR
NffHGrWzWWgDBfTRhChCnSCWcnjT
QrlQBPBrlPHrrQlrHFLqPnLvVvbVmVVJtq
MVMpHMZLVCpMrfWjvWnfrJ
hlblzDDzwlSlGtRhRlSdrfGGWnWWfFPjJjnfqWGF
lmlhBRlDhhhDRRhwDmBpHJmsNCHmCgNHJCJLsc
jvsLgmqLgHvbPPVbNjSCjC
pwTcRpRWLRMLJJFwBBGWcFWNVlDDCSTVttNPblZZCVVDlP
GcdhccpcpRpGRhGmfsHHzLQQHrmsnh
FMmSRgtMltMnVgnmNvlrsJrsZWjspvsZJp
QbdhqwqbNqdHbTdcbcpsrpvjfWfLJLfwJrWp
DQBBQqQGccdTPGqqBNtFGRSMRSFGtnVSnnmM
fPjGrfFrrprprdrbQPZwlcZwZmlJwH
qvNnvWnvWDvSvqNtWSLWStqbcJBQwQJwQZHLBZbcmJbblb
DMtvqSvvDtntCRfwzGCgdzzFjG
TfdZgtmfDgqgvlLFFsFHvcvZ
pphWQMVjQVVBWWjRlHlHnlcLDDhcnF
JQwwWVPBwMJpJwpWwGBWNzrDzSSzfgTPqTSTTtSPgt
"""
puzzleInput = puzzleInput.split()
hell = ValueError
letters = []
for i, letter in enumerate(string.ascii_letters):
    letters.append([letter, i+1])
def getCharPriority(char):
    for i in range(len(letters)):
        if char == letters[i][0]:
            return letters[i][1]
comps = []
for i in range(len(puzzleInput)):
    cLength = int(len(puzzleInput[i])/2)
    comps.append([puzzleInput[i][:cLength], puzzleInput[i][cLength:]])
priorities = 0
for i in range(len(comps)):
    breakLoop = False
    for j in range(len(comps[i][0])):
        if breakLoop: break
        for k in range(len(comps[i][1])):
            if breakLoop: break
            if comps[i][0][j] == comps[i][1][k]:
                breakLoop = True
                priorities += getCharPriority(comps[i][0][j])
print(priorities)
priorities = 0
for i in range(int(len(puzzleInput)/3)):
    breakLoop = False
    ind1 = int(3*i)
    ind2 = int(3*i+1)
    ind3 = int(3*i+2)
    for j in range(len(puzzleInput[ind1])):
        if breakLoop: break
        for k in range(len(puzzleInput[ind2])):
            if breakLoop: break
            for m in range(len(puzzleInput[ind3])):
                if breakLoop: break
                if puzzleInput[ind1][j] == puzzleInput[ind2][k] == puzzleInput[ind3][m]:
                    breakLoop = True
                    priorities += getCharPriority(puzzleInput[ind1][j])
print(priorities)