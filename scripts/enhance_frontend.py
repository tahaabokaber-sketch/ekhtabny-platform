from pathlib import Path

path = Path('/home/ubuntu/ekhtabny-platform/client/src/App.tsx')
s = path.read_text()

s = s.replace('  Activity,\n', '  Activity,\n  BrainCircuit,\n  LineChart,\n  LoaderCircle,\n')
s = s.replace('type ToastType = "success" | "error" | "info";', 'type ToastType = "success" | "error" | "info" | "loading";')
s = s.replace('type StudentView = "dashboard" | "exams" | "history" | "profile" | "details" | "preview" | "taking" | "result";', 'type StudentView = "dashboard" | "exams" | "history" | "analytics" | "profile" | "details" | "preview" | "taking" | "result";')

s = s.replace('const icon = toast.type === "success" ? <CheckCircle2 size={18} /> : toast.type === "error" ? <AlertCircle size={18} /> : <Zap size={18} />;', 'const icon = toast.type === "success" ? <CheckCircle2 size={18} /> : toast.type === "error" ? <AlertCircle size={18} /> : toast.type === "loading" ? <LoaderCircle className="spin-icon" size={18} /> : <Zap size={18} />;')
s = s.replace('  const [studentView, setStudentView] = useState<StudentView>("dashboard");', '  const [studentView, setStudentView] = useState<StudentView>("dashboard");')

s = s.replace('const items = [{ id: "dashboard", label: "الرئيسية", icon: House }, { id: "exams", label: "الامتحانات", icon: FileText, badge: "3" }, { id: "history", label: "سجل النتائج", icon: History }, { id: "profile", label: "الملف الشخصي", icon: UserRound }];', 'const items = [{ id: "dashboard", label: "الرئيسية", icon: House }, { id: "exams", label: "الامتحانات", icon: FileText, badge: "3" }, { id: "history", label: "سجل النتائج", icon: History }, { id: "analytics", label: "تحليلات الأداء", icon: LineChart }, { id: "profile", label: "الملف الشخصي", icon: UserRound }];')
s = s.replace('{view === "history" && <StudentHistory attempts={attempts} exams={exams} setSelectedAttempt={(a) => { setSelectedAttempt(a); setSelectedExam(exams.find(e => e.id === a.examId) || exams[0]); setView("result"); }} />}{view === "profile"', '{view === "history" && <StudentHistory attempts={attempts} exams={exams} setSelectedAttempt={(a) => { setSelectedAttempt(a); setSelectedExam(exams.find(e => e.id === a.examId) || exams[0]); setView("result"); }} />}{view === "analytics" && <StudentAnalytics attempts={attempts} exams={exams} />}{view === "profile"')

marker = 'function ProfilePage({ notify }: { notify: (m: string, t?: ToastType) => void }) {'
analytics = r'''function StudentAnalytics({ attempts, exams }: { attempts: Attempt[]; exams: Exam[] }) {
  const subjectRows = [
    { subject: "الرياضيات", values: [68, 74, 79, 84], tone: "blue" },
    { subject: "العلوم", values: [72, 78, 82, 87], tone: "teal" },
    { subject: "اللغة العربية", values: [61, 69, 73, 76], tone: "violet" },
    { subject: "اللغة الإنجليزية", values: [70, 76, 80, 84], tone: "orange" },
  ];
  const average = Math.round(attempts.reduce((sum, item) => sum + item.percentage, 0) / attempts.length);
  return <><PageIntro eyebrow="رؤية أوضح لتقدمك" title="تحليلات الأداء" text="تابع تطور مستواك في كل مادة واكتشف أين تضع مجهودك القادم." action={<div className="analytics-period"><CalendarDays size={15} /> آخر ٣ أشهر <ChevronDown size={14} /></div>} />
    <div className="analytics-kpis"><StatCard label="متوسط الأداء العام" value={`${average}%`} icon={LineChart} tone="blue" hint="تحسن ٦٪ عن الشهر الماضي" /><StatCard label="المواد المتقدمة" value="3" icon={Trophy} tone="teal" hint="من أصل ٤ مواد" /><StatCard label="أيام المذاكرة" value="18" icon={CalendarDays} tone="violet" hint="هذا الشهر" /><StatCard label="وقت المراجعة" value="12.5س" icon={Clock3} tone="orange" hint="+٢.٣س عن الشهر السابق" /></div>
    <div className="content-grid analytics-top-grid"><section className="panel performance-chart"><div className="panel-heading"><div><div className="section-kicker">تطور متوسط الدرجات</div><h2>منحنى أدائك عبر الوقت</h2></div><div className="chart-legend"><span><i className="legend-dot blue" />متوسطك</span><span><i className="legend-dot teal" />المعدل المستهدف</span></div></div><div className="line-chart"><div className="chart-y-labels"><span>100</span><span>80</span><span>60</span><span>40</span></div><div className="line-chart-body"><div className="chart-grid-lines"><i /><i /><i /><i /><i /></div><svg viewBox="0 0 600 180" preserveAspectRatio="none" aria-label="منحنى تطور الأداء"><polyline points="0,120 100,104 200,112 300,72 400,80 500,45 600,52" fill="none" stroke="#3b6fe8" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" /><polyline points="0,92 100,88 200,84 300,80 400,76 500,72 600,68" fill="none" stroke="#8bd6c7" strokeWidth="3" strokeDasharray="7 8" strokeLinecap="round" /></svg><div className="chart-dots">{[[0,120],[100,104],[200,112],[300,72],[400,80],[500,45],[600,52]].map(([left, top], i) => <i key={i} style={{ left: `${(left / 600) * 100}%`, top: `${(top / 180) * 100}%` }} />)}</div><div className="chart-x-labels"><span>يونيو</span><span>يوليو</span><span>أغسطس</span><span>سبتمبر</span><span>أكتوبر</span><span>نوفمبر</span><span>ديسمبر</span></div></div></div></section><section className="panel insight-panel"><div className="panel-heading"><div><div className="section-kicker">ملاحظة ذكية</div><h2>تحليل مختصر</h2></div><BrainCircuit size={19} className="insight-icon" /></div><div className="insight-highlight"><Sparkles size={18} /><strong>أداؤك يتطور بثبات</strong><span>تحسن متوسطك العام ٦٪ خلال آخر ٣ أشهر.</span></div><div className="insight-item"><div className="insight-mini blue"><Trophy size={16} /></div><div><strong>نقطة قوتك: العلوم</strong><span>متوسطك ٨٧٪، استمر على نفس أسلوب المراجعة.</span></div></div><div className="insight-item"><div className="insight-mini orange"><Zap size={16} /></div><div><strong>فرصة التحسين: اللغة العربية</strong><span>حل ٣ تمارين إضافية أسبوعياً لرفع مستواك.</span></div></div></section></div>
    <section className="panel subject-progress-panel"><div className="panel-heading"><div><div className="section-kicker">مقارنة المواد</div><h2>تقدمك في كل مادة</h2></div><button className="soft-btn">عرض التفاصيل <ArrowLeft size={15} /></button></div><div className="subject-chart">{subjectRows.map(row => <div className="subject-chart-row" key={row.subject}><div className="subject-chart-label"><div className={cn("subject-icon small", `accent-${row.tone}`)}>{row.subject === "الرياضيات" ? "∑" : row.subject === "العلوم" ? "⚗" : row.subject === "اللغة العربية" ? "ع" : "A"}</div><strong>{row.subject}</strong></div><div className="subject-bars">{row.values.map((value, i) => <div className="subject-bar-wrap" key={i}><span className={row.tone} style={{ height: `${value}%` }} /><small>{value}%</small></div>)}</div><strong className="subject-current">{row.values[row.values.length - 1]}%</strong></div>)}</div><div className="subject-axis"><span>الاختبار ١</span><span>الاختبار ٢</span><span>الاختبار ٣</span><span>آخر نتيجة</span></div></section>
    <div className="analytics-footer-note"><BrainCircuit size={16} /><span>التحليلات مبنية على نتائجك المحفوظة في هذا الجهاز، ويمكن ربطها لاحقاً ببيانات المركز الفعلية.</span></div></>;
}

'''
s = s.replace(marker, analytics + marker)

old = 'const [step, setStep] = useState(1); const [title, setTitle] = useState(""); const [subject, setSubject] = useState(subjects[0]); const [grade, setGrade] = useState(grades[5]); const [duration, setDuration] = useState("45"); const [questionCount, setQuestionCount] = useState(5); const [uploaded, setUploaded] = useState(false); const [rows, setRows] = useState<{ type: string; answer: string; marks: string }[]>([]);'
new = 'const [step, setStep] = useState(1); const [title, setTitle] = useState(""); const [subject, setSubject] = useState(subjects[0]); const [grade, setGrade] = useState(grades[5]); const [duration, setDuration] = useState("45"); const [questionCount, setQuestionCount] = useState(5); const [uploaded, setUploaded] = useState(false); const [sourceText, setSourceText] = useState(""); const [aiLoading, setAiLoading] = useState(false); const [isSaving, setIsSaving] = useState(false); const [rows, setRows] = useState<{ question: string; type: string; answer: string; marks: string }[]>([]);'
s = s.replace(old, new)
old2 = 'const next = () => { if (step === 1 && !title.trim()) { notify("أدخل عنوان الامتحان أولاً", "error"); return; } if (step < 5) setStep(step + 1); else { setExams(prev => [{ id: Date.now(), title, subject, grade, date: "يُحدد لاحقاً", duration: Number(duration), questions: questionCount, marks: questionCount * 2, status: "لم يبدأ", teacher: "أ/ محمد السيد", participants: 0, accent: "blue" }, ...prev]); notify("تم إنشاء الامتحان وحفظه كمسودة"); setView("exams"); } }; const generate = () => { setRows(Array.from({ length: questionCount }, (_, i) => ({ type: i % 3 === 0 ? "صح أم خطأ" : "اختيار من متعدد", answer: "", marks: "2" }))); notify(`تم توليد ${questionCount} صفوف للإجابة`, "info"); };'
new2 = 'const next = () => { if (step === 1 && !title.trim()) { notify("أدخل عنوان الامتحان أولاً", "error"); return; } if (step < 5) setStep(step + 1); else { setIsSaving(true); notify("جارٍ حفظ الامتحان كمسودة...", "loading"); window.setTimeout(() => { setExams(prev => [{ id: Date.now(), title, subject, grade, date: "يُحدد لاحقاً", duration: Number(duration), questions: questionCount, marks: questionCount * 2, status: "لم يبدأ", teacher: "أ/ محمد السيد", participants: 0, accent: "blue" }, ...prev]); setIsSaving(false); notify("تم إنشاء الامتحان وحفظه كمسودة"); setView("exams"); }, 900); } }; const generate = () => { setRows(Array.from({ length: questionCount }, (_, i) => ({ question: "", type: i % 3 === 0 ? "صح أم خطأ" : "اختيار من متعدد", answer: "", marks: "2" }))); notify(`تم توليد ${questionCount} صفوف للإجابة`, "info"); }; const generateFromText = () => { const seed = sourceText.trim().split(/[.!؟]/)[0] || title || "المحتوى التعليمي"; setAiLoading(true); notify("جارٍ تحليل النص وتوليد أسئلة اختيار من متعدد...", "loading"); window.setTimeout(() => { const generated = Array.from({ length: Math.min(5, Math.max(3, questionCount)) }, (_, i) => ({ question: `${seed} — ما العبارة الأدق التي تعبّر عن الفكرة الأساسية؟`, type: "اختيار من متعدد", answer: i % 2 === 0 ? "الخيار أ" : "الخيار ب", marks: "2" })); setQuestionCount(generated.length); setRows(generated); setAiLoading(false); notify(`تم توليد ${generated.length} أسئلة من النص بنجاح`); }, 1100); };'
s = s.replace(old2, new2)
s = s.replace('<div className="form-section-head"><div className="section-kicker">الخطوة ٣ من ٥</div><h2>نموذج الإجابات</h2><p>أدخل الإجابات الصحيحة يدوياً — المنصة لا تقرأ محتوى PDF تلقائياً.</p></div><div className="answer-generator">', '<div className="form-section-head"><div className="section-kicker">الخطوة ٣ من ٥</div><h2>نموذج الإجابات</h2><p>ولّد أسئلة اختيار من متعدد من نص الدرس أو أدخل الإجابات الصحيحة يدوياً.</p></div><div className="ai-generator-card"><div className="ai-generator-head"><div className="ai-generator-icon"><BrainCircuit size={20} /></div><div><strong>مولّد الأسئلة الذكي <span>Demo AI</span></strong><p>محاكاة محلية: لا يتم إرسال النص خارج المتصفح.</p></div></div><textarea value={sourceText} onChange={e => setSourceText(e.target.value)} placeholder="الصق هنا فقرة الدرس أو ملخص الوحدة... مثال: الطاقة لا تفنى ولا تستحدث من العدم، ولكنها تتحول من صورة إلى أخرى." /><button className="primary-btn ai-generate-btn" onClick={generateFromText} disabled={aiLoading}><BrainCircuit size={17} />{aiLoading ? "جارٍ التوليد..." : "توليد أسئلة من النص"}{aiLoading && <LoaderCircle className="spin-icon" size={16} />}</button></div><div className="answer-generator">')
s = s.replace('<input placeholder="الإجابة الصحيحة" value={row.answer}', '<input placeholder="نص السؤال الناتج" value={row.question} onChange={e => setRows(rows.map((r, j) => j === i ? { ...r, question: e.target.value } : r))} /><input placeholder="الإجابة الصحيحة" value={row.answer}')
s = s.replace('<button className="primary-btn" onClick={next}>{step === 5 ? "حفظ كمسودة" : "التالي"} <ArrowLeft size={16} /></button>', '<button className="primary-btn" onClick={next} disabled={isSaving}>{isSaving ? <><LoaderCircle className="spin-icon" size={16} /> جارٍ الحفظ...</> : <>{step === 5 ? "حفظ كمسودة" : "التالي"} <ArrowLeft size={16} /></>}</button>')

s = s.replace('const [current, setCurrent] = useState(0); const [answers, setAnswers] = useState<Record<number, string>>({}); const [marked, setMarked] = useState<number[]>([]); const [seconds, setSeconds] = useState(exam.duration * 60); const [confirm, setConfirm] = useState(false);', 'const [current, setCurrent] = useState(0); const [answers, setAnswers] = useState<Record<number, string>>({}); const [marked, setMarked] = useState<number[]>([]); const [seconds, setSeconds] = useState(exam.duration * 60); const [confirm, setConfirm] = useState(false); const [isSubmitting, setIsSubmitting] = useState(false);')
old3 = 'const submit = () => { const correct = questions.filter(q => answers[q.id] === q.answer).length; const unanswered = questions.length - answered; const wrong = answered - correct; const percentage = Math.round((correct / questions.length) * 100); saveAttempt({ id: Date.now(), examId: exam.id, score: Math.round((percentage / 100) * exam.marks), percentage, correct, wrong, unanswered, date: "اليوم، ١٨ سبتمبر ٢٠٢٥" }); };'
new3 = 'const submit = () => { if (isSubmitting) return; setIsSubmitting(true); notify("جارٍ تصحيح إجاباتك وحفظ النتيجة...", "loading"); const correct = questions.filter(q => answers[q.id] === q.answer).length; const unanswered = questions.length - answered; const wrong = answered - correct; const percentage = Math.round((correct / questions.length) * 100); window.setTimeout(() => { saveAttempt({ id: Date.now(), examId: exam.id, score: Math.round((percentage / 100) * exam.marks), percentage, correct, wrong, unanswered, date: "اليوم، ١٨ سبتمبر ٢٠٢٥" }); setIsSubmitting(false); notify("تم حفظ النتيجة بنجاح"); }, 1000); };'
s = s.replace(old3, new3)
s = s.replace('<button className="primary-btn" onClick={submit}>تأكيد التسليم <Check size={16} /></button>', '<button className="primary-btn" onClick={submit} disabled={isSubmitting}>{isSubmitting ? <><LoaderCircle className="spin-icon" size={16} /> جارٍ التصحيح...</> : <>تأكيد التسليم <Check size={16} /></>}</button>')

path.write_text(s)

css = Path('/home/ubuntu/ekhtabny-platform/client/src/index.css')
c = css.read_text()
c += r'''

/* AI question generator, analytics and loading states */
.spin-icon { animation: spin 1s linear infinite; }
.toast-loading svg:first-child { color: var(--blue); }
.ai-generator-card { padding: 17px; margin-bottom: 17px; background: linear-gradient(135deg, #f4f7ff, #f4fbfa); border: 1px solid #dce7fa; border-radius: 14px; }
.ai-generator-head { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.ai-generator-icon { width: 36px; height: 36px; display: grid; place-items: center; color: var(--violet); background: #ebe8ff; border-radius: 10px; }
.ai-generator-head > div:last-child { display: grid; gap: 3px; }
.ai-generator-head strong { color: var(--navy); font-size: 12px; }
.ai-generator-head strong span { margin-right: 5px; padding: 3px 5px; color: var(--violet); background: #ebe8ff; border-radius: 5px; font: 700 8px Inter, Arial, sans-serif; }
.ai-generator-head p { margin: 0; color: #8997aa; font-size: 9px; }
.ai-generator-card textarea { min-height: 86px; margin-bottom: 10px; background: rgba(255,255,255,.75); }
.ai-generate-btn { min-height: 37px; background: linear-gradient(100deg, #4d5edc, #198e9b); }
.ai-generate-btn:disabled { opacity: .72; }
.analytics-period { display: flex; align-items: center; gap: 7px; padding: 9px 11px; color: #62718a; border: 1px solid var(--line); border-radius: 9px; background: #fff; font-size: 10px; }
.analytics-kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 13px; margin-bottom: 20px; }
.analytics-top-grid { grid-template-columns: minmax(0, 1.35fr) minmax(300px, .65fr); }
.performance-chart { min-height: 295px; }
.performance-chart .chart-legend { margin: 0; }
.line-chart { display: flex; height: 200px; margin-top: 22px; }
.chart-y-labels { display: flex; flex-direction: column; justify-content: space-between; padding: 0 10px 25px 0; color: #a1abb9; font: 9px Inter, Arial, sans-serif; }
.line-chart-body { position: relative; flex: 1; margin-right: 3px; }
.chart-grid-lines { position: absolute; inset: 0 0 25px; display: flex; flex-direction: column; justify-content: space-between; }
.chart-grid-lines i { display: block; height: 1px; background: #edf0f5; }
.line-chart-body svg { position: absolute; inset: 0 0 25px; width: 100%; height: calc(100% - 25px); overflow: visible; }
.chart-dots { position: absolute; inset: 0 0 25px; }
.chart-dots i { position: absolute; width: 9px; height: 9px; background: #fff; border: 3px solid var(--blue); border-radius: 50%; transform: translate(-50%, -50%); }
.chart-x-labels { position: absolute; right: 0; bottom: 0; left: 0; display: flex; justify-content: space-between; color: #9da8b6; font-size: 9px; }
.insight-panel { min-height: 295px; }
.insight-icon { color: var(--violet); }
.insight-highlight { display: grid; grid-template-columns: auto 1fr; column-gap: 9px; padding: 13px; margin: 18px 0 15px; color: #53657d; background: #f3f1ff; border-radius: 11px; }
.insight-highlight svg { grid-row: span 2; color: var(--violet); }
.insight-highlight strong { color: #5544af; font-size: 11px; }
.insight-highlight span { color: #8a82b4; font-size: 9px; }
.insight-item { display: flex; align-items: center; gap: 9px; padding: 12px 0; border-top: 1px solid #f0f2f6; }
.insight-item > div:last-child { display: grid; gap: 4px; }
.insight-item strong { color: var(--navy); font-size: 10px; }
.insight-item span { color: #96a2b2; font-size: 9px; line-height: 1.5; }
.insight-mini { width: 30px; height: 30px; display: grid; place-items: center; flex: 0 0 auto; border-radius: 9px; }
.insight-mini.blue { color: var(--blue); background: #eaf0ff; }.insight-mini.orange { color: var(--orange); background: #fff2df; }
.subject-progress-panel { padding: 23px !important; margin-bottom: 16px; }
.subject-chart { display: grid; gap: 16px; margin-top: 23px; }
.subject-chart-row { display: grid; grid-template-columns: 175px 1fr 50px; align-items: center; gap: 14px; }
.subject-chart-label { display: flex; align-items: center; gap: 9px; }.subject-chart-label strong { color: #51617a; font-size: 10px; }
.subject-bars { display: flex; align-items: end; gap: 8px; height: 43px; padding: 0 6px; border-bottom: 1px solid #edf0f4; }
.subject-bar-wrap { position: relative; display: flex; align-items: end; justify-content: center; height: 100%; flex: 1; }
.subject-bar-wrap span { display: block; width: 100%; max-width: 24px; min-height: 5px; border-radius: 4px 4px 0 0; }.subject-bar-wrap span.blue { background: #79a0ef; }.subject-bar-wrap span.teal { background: #69c9b7; }.subject-bar-wrap span.violet { background: #a497eb; }.subject-bar-wrap span.orange { background: #edba76; }
.subject-bar-wrap small { position: absolute; top: -16px; color: #8b98aa; font: 8px Inter, Arial, sans-serif; }
.subject-current { color: var(--navy); font: 800 14px Inter, Arial, sans-serif; text-align: left; }
.subject-axis { display: flex; justify-content: space-between; padding-right: 190px; padding-left: 50px; color: #a0a9b7; font-size: 8px; }
.analytics-footer-note { display: flex; align-items: center; gap: 8px; color: #829b95; font-size: 10px; }.analytics-footer-note svg { color: var(--teal); }
@media (max-width: 900px) { .analytics-top-grid { grid-template-columns: 1fr; }.analytics-kpis { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 620px) { .analytics-period { width: 100%; justify-content: center; }.subject-chart-row { grid-template-columns: 125px 1fr 40px; gap: 7px; }.subject-axis { padding-right: 135px; padding-left: 40px; }.subject-chart-label strong { font-size: 9px; }.subject-bars { gap: 4px; }.ai-generator-card { padding: 13px; } }
'''
css.write_text(c)
