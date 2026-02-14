import React, { useState } from 'react';
import { Trophy, Calendar, Users, Star, Moon, Medal, ChevronRight, Award } from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState('qualifiers');

  const matches = [
    { id: 1, day: '1 رمضان', teamA: 'عبدالعزيز حزام & هاني', teamB: 'نايف & سالم', stage: 'qualifiers' },
    { id: 2, day: '3 رمضان', teamA: 'عزوز & تركي ناصر', teamB: 'خالد & باسم', stage: 'qualifiers' },
    { id: 3, day: '5 رمضان', teamA: 'فادي & ريان فيحان', teamB: 'مشعل & ماجد', stage: 'qualifiers' },
    { id: 4, day: '7 رمضان', teamA: 'عبدالرحمن & متعب', teamB: 'بسام & معاذ', stage: 'qualifiers' },
    { id: 5, day: '9 رمضان', teamA: 'بشار & عمر ناصر', teamB: 'أيمن & راكان', stage: 'qualifiers' },
    { id: 6, day: '11 رمضان', teamA: 'محمد & مشاري', teamB: 'ماجد منصور & ريان', stage: 'qualifiers' },
    { id: 7, day: '13 رمضان', teamA: 'تركي فريح & عبدالسلام', teamB: 'شادي & أمجد', stage: 'qualifiers' },
  ];

  const semiFinals = [
    { id: 8, day: '18 رمضان', title: 'نصف النهائي الأول', teamA: 'فائز (1)', teamB: 'فائز (2)', stage: 'semi' },
    { id: 9, day: '20 رمضان', title: 'نصف النهائي الثاني', teamA: 'فائز (3)', teamB: 'فائز (4)', stage: 'semi' },
    { id: 10, day: '22 رمضان', title: 'نصف النهائي الثالث', teamA: 'فائز (5)', teamB: 'فائز (6)', stage: 'semi' },
    { id: 11, day: '24 رمضان', title: 'مواجهة الملحق', teamA: 'فائز (7)', teamB: 'أفضل خاسر', stage: 'semi' },
  ];

  const finalStages = [
    { id: 12, day: '27 رمضان', title: 'المربع الذهبي', desc: 'مواجهة حاسمة بين المتأهلين من نصف النهائي' },
    { id: 13, day: '29 رمضان', title: 'النهائي الكبير', desc: 'تحديد بطل دوري الحروف الرمضاني' },
  ];

  const StageCard = ({ match, type }) => (
    <div className="bg-slate-800/50 border border-amber-500/30 rounded-xl p-6 mb-4 hover:border-amber-400 transition-all cursor-default group overflow-hidden relative">
      <div className="absolute top-0 right-0 w-16 h-16 bg-amber-500/5 rounded-bl-full flex items-start justify-end p-2">
        <Moon className="w-4 h-4 text-amber-500/40" />
      </div>

      <div className="flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="bg-amber-600 p-2 rounded-lg">
            <Calendar className="w-5 h-5 text-white" />
          </div>
          <div>
            <p className="text-amber-400 text-sm font-bold">{match.day}</p>
            <h3 className="text-white font-semibold">{match.title || `المواجهة رقم ${match.id}`}</h3>
          </div>
        </div>

        <div className="flex items-center gap-4 flex-1 justify-center px-4">
          <div className="text-center flex-1">
            <p className="text-white font-medium text-lg">{match.teamA}</p>
          </div>
          <div className="bg-amber-500/20 px-3 py-1 rounded-full text-amber-500 font-black text-xs">VS</div>
          <div className="text-center flex-1">
            <p className="text-white font-medium text-lg">{match.teamB}</p>
          </div>
        </div>

        <div className="bg-slate-700/50 px-4 py-2 rounded-lg border border-slate-600">
          <span className="text-slate-300 text-sm flex items-center gap-2">
            <Users className="w-4 h-4" /> فريقين
          </span>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-950 text-right font-sans p-4 md:p-8" dir="rtl">
      <div className="max-w-5xl mx-auto mb-12 text-center">
        <div className="flex justify-center mb-4">
          <div className="relative">
            <Trophy className="w-20 h-20 text-amber-500 animate-pulse" />
            <Star className="absolute -top-2 -right-2 text-yellow-300 w-8 h-8 fill-current" />
          </div>
        </div>
        <h1 className="text-4xl md:text-6xl font-black text-white mb-4 tracking-tighter">
          تحدي <span className="text-amber-500">حروف</span> الرمضاني
        </h1>
        <p className="text-slate-400 text-lg max-w-2xl mx-auto">
          مواجهات ثنائية، ذكاء وسرعة، وبطل واحد يتربع على عرش المنافسة في ليلة العيد.
        </p>
      </div>

      <div className="max-w-4xl mx-auto mb-8 flex justify-center gap-2 p-1 bg-slate-900 rounded-2xl border border-slate-800">
        {[
          { id: 'qualifiers', label: 'التصفيات (دور 14)' },
          { id: 'semi', label: 'الأدوار النهائية' },
          { id: 'grand-final', label: 'منصة التتويج' }
        ].map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-6 py-3 rounded-xl font-bold transition-all flex-1 ${
              activeTab === tab.id
                ? 'bg-amber-600 text-white shadow-lg shadow-amber-900/20'
                : 'text-slate-500 hover:text-slate-300'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div className="max-w-4xl mx-auto">
        {activeTab === 'qualifiers' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="mb-6 flex items-center justify-between">
              <h2 className="text-2xl font-bold text-white flex items-center gap-2">
                <Star className="text-amber-500" /> مواجهات المرحلة الأولى
              </h2>
              <span className="text-slate-500 text-sm italic">7 مواجهات حاسمة</span>
            </div>
            {matches.map(match => (
              <StageCard key={match.id} match={match} />
            ))}
          </div>
        )}

        {activeTab === 'semi' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="mb-6 flex items-center justify-between">
              <h2 className="text-2xl font-bold text-white flex items-center gap-2">
                <Medal className="text-amber-500" /> الطريق إلى النهائي
              </h2>
            </div>
            {semiFinals.map(match => (
              <StageCard key={match.id} match={match} />
            ))}
          </div>
        )}

        {activeTab === 'grand-final' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 text-center py-10">
            <div className="bg-gradient-to-b from-amber-600/20 to-transparent border border-amber-500/20 rounded-3xl p-12">
              <Award className="w-24 h-24 text-amber-500 mx-auto mb-6" />
              <h2 className="text-4xl font-black text-white mb-8">المواجهات الختامية</h2>

              <div className="space-y-6">
                {finalStages.map(stage => (
                  <div key={stage.id} className="bg-slate-800 border-l-4 border-amber-600 p-6 rounded-r-xl text-right">
                    <div className="flex items-center justify-between">
                      <div>
                        <span className="text-amber-500 font-bold block mb-1">{stage.day}</span>
                        <h3 className="text-2xl font-bold text-white">{stage.title}</h3>
                        <p className="text-slate-400">{stage.desc}</p>
                      </div>
                      <ChevronRight className="text-slate-600" />
                    </div>
                  </div>
                ))}
              </div>

              <div className="mt-12 p-6 border-t border-amber-500/20">
                <p className="text-amber-400 font-bold text-xl uppercase tracking-widest">فريق واحد فقط سيحمل الكأس</p>
                <div className="flex justify-center gap-4 mt-4">
                   <div className="w-12 h-1 bg-amber-600 rounded-full"></div>
                   <div className="w-12 h-1 bg-amber-600 rounded-full"></div>
                   <div className="w-12 h-1 bg-amber-600 rounded-full"></div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="mt-20 text-center opacity-30 pointer-events-none">
        <p className="text-slate-500 italic text-sm">جميع الحقوق محفوظة - بطولة الحروف 1445هـ</p>
      </div>
    </div>
  );
};

export default App;
